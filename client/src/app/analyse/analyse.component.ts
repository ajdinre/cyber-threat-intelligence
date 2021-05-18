import { AfterViewInit, Component, ViewChild, ElementRef } from '@angular/core';
import {MatPaginator} from '@angular/material/paginator';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import {FlexLayoutModule} from '@angular/flex-layout';
import { FormControl } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { FileService } from '../shared/services/file.service';
import { HttpClient, HttpParams } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import * as d3 from 'd3';
import { IpAddress } from '../shared/components/classes/ipadrress';




@Component({
  selector: 'app-analyse',
  templateUrl: './analyse.component.html',
  styleUrls: ['./analyse.component.css']
})
export class AnalyseComponent implements AfterViewInit{
  serverNames = new FormControl();
  chosenServerNamesList : string[] = [];
  private csrf : any;
  serverNamesList : string[] = [];
  searchIpAddressesQuery : string = '';
  ipInputList : string = '';
  testIpRow = new IpAddress();
  testIpData : IpAddress[] = [];
  @ViewChild('graphContainer') graphContainer: ElementRef;
  nodes :any[] = [];
  APIlinks: any[] = [];

  width = 500;
  height = 500;
  colors = ["rgb(255, 95, 57)", "rgb(177, 125, 245)", "rgb(224, 97, 152)", "rgb(129, 89, 255)"];
  stroke_colors = ["rgb(224, 95, 57)", "rgb(164, 113, 229)", "rgb(208, 97, 128)", "rgb(101, 69, 223)"];

  links = [{source: this.nodes[0], target: this.nodes[1]}];
  svg: any;
  force: any;
  path: any;
  circle: any;
  tooltip: any;
  label: any;

  selectedNode = null;
  selectedLink = null;


  displayedColumns: string[] = ['ip_address', 'host_name', 'org', 'city', 'region', 'country', 'postal','time_zone','latitude','longitude'];
  dataSource: MatTableDataSource<IpAddress>;
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private fileService : FileService,
    private cookieService : CookieService,
    private httpParams : HttpParams
  ) {
    this.csrf = this.cookieService.get("csrftoken");
      if (typeof(this.csrf) === 'undefined'){
        this.csrf = '';
      }
    this.getServerNames();
    this.dataSource = new MatTableDataSource();
  }

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  onSelect(data): void {
    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  onActivate(data): void {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  onDeactivate(data): void {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));

  }

  getServerNames(){
    this.fileService.getServerNames().subscribe((res : any) => {
      res.forEach(item => {
        this.serverNamesList.push(item.toString());
      })
    });
  }
  searchWithNeo4j(){
    const chosenServerNames = this.chosenServerNamesList.join(',');


    //Mat Table data request
    this.fileService.getFilteredDataForMatTable(chosenServerNames, this.searchIpAddressesQuery)
      .subscribe((res)=>{
        this.dataSource = new MatTableDataSource(res);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      });

      this.cleanUpD3Canvas();
    //Neo4j nodes data request
    this.fileService.getFilteredDataForNeoNodes(chosenServerNames, this.searchIpAddressesQuery)
      .subscribe((res)=>{
        console.log(res);
        this.nodes = res;
      });

    //Neo4j APIlinks data request
    this.fileService.getFilteredDataForNeoAPIlinks(chosenServerNames, this.searchIpAddressesQuery)
      .subscribe((res)=>{
        console.log(res);
        this.APIlinks = res;
      });
      setTimeout(() =>{ this.ngAfterContentInit()}, 500);
  }

  searchWithGrafana(){
    console.log("Search with Grafana Button Clicked!")
  }
  searchWithKibana(){
    console.log("Search with Kibana Button Clicked!")


}

  // d3 code
  cleanUpD3Canvas() {
    var d3container = document.getElementById("graphContainer");

    while (d3container?.firstChild) {
      d3container.querySelectorAll('*').forEach(n => n.remove());
    }
    while(this.links.length > 0) {
      this.links.pop()
    }
    while(this.nodes.length > 0) {
      this.nodes.pop()
    }
    while(this.APIlinks.length > 0) {
      this.APIlinks.pop()
    }
  }

  ngAfterContentInit() {
    this.width = document.getElementById('neo4j-content-container')!.clientWidth;
    // reformating links
    this.links.pop()
    this.APIlinks.forEach(r => {
      if(r[1] == 'HAS_SENT') {
        this.links.push({ "source": r[0]['ip_address'], 'target': r[2]['path'] })
      } else if (r[1] == 'HAS_ACCESSED') {
        this.links.push({ 'source': r[0]['path'], 'target': r[2]['server_name'] })
      }
    });

    // draw graph container
    this.svg = d3.select('#graphContainer')
      .attr('oncontextmenu', 'return false;')
      .attr('width', this.width)
      .attr('height', this.height);



    setTimeout(() =>{ this.simulate()}, 2000);

    setTimeout(() =>{ this.restart()}, 4000);
  }

  simulate() {
    this.force = d3.forceSimulation()
      .force('link', d3.forceLink().id((d: any) => d.id).distance(150))
      .force('charge', d3.forceManyBody().strength(-500))
      .force('x', d3.forceX(this.width / 2))
      .force('y', d3.forceY(this.height / 2))
      .on('tick', () => this.tick());


    // handles to link and node element groups
    this.path = this.svg.append('svg:g').selectAll('path');
    this.circle = this.svg.append('svg:g').selectAll('g');
  }


  // update force layout
  tick() {
    // draw edges
    this.path.attr('d', (d: any) => {
      return `M${d.source.x},${d.source.y}L${d.target.x},${d.target.y}`;
    });


    this.circle.attr('transform', (d) => `translate(${d.x},${d.y})`);
  }

  // update graph
  restart() {
    // draw links
    this.path = this.path.data(this.links).enter()
      .append('svg:path')
      .attr('class', 'link')
      //.classed('selected', (d) => d === this.selectedLink)
      .merge(this.path);


    // circle (node) group
    // NB: the function arg is crucial here! nodes are known by name, not by index!
    this.circle = this.circle.data(this.nodes, (d) => d.id);

    // draw nodes
    const g = this.circle.enter().append('svg:g');

    g.append('svg:circle')
      .attr('class', 'node')
      .attr('r', function(d) { return d.count != null ? d.count + 10 : 10; })
      .style('fill', (d) => {
        return this.colors[d.group%this.colors.length];
      })
      .style('stroke', (d) => {
        return this.stroke_colors[d.group%this.stroke_colors.length];
      })

    this.svg.selectAll("circle")
      .call(
        d3.drag()
        .on("start", (event, d) => {this.dragstarted(event, d);})
        .on("drag", (event, d) => {this.dragged(event, d);})
        .on("end", (event, d) => {this.dragended(event, d);})
      );



    this.tooltip = d3.select("#neo4j-mat-card")
      .append("div")
      .attr("class", "label")
      .style("position", "absolute")
      .style("visibility", "hidden")
      .style("color", "white")
      .style("padding", "8px")
      .style("background-color", "#626D71")
      .style("border-radius", "6px")
      .style("text-align", "center")
      .style("width", "auto")
      .text("");

    // shows a label/name of every node
    g.append('svg:text')
      .attr('x', 0)
      .attr('y', 4)
      .attr('class', 'node-text')
      .style("fill", "#fff")
      .text((d) => {
        if(d.ip_address != null || d.server_name != null) { return d.id; }
        else { return ''; }
      })
    this.circle = g.merge(this.circle);

    //show tooltip
    this.circle
      .on('mouseover', (event, d) => {
        var node_details = '<div style="text-align: left;">';
        for (const key in d) {
          if(key !== 'x' && key !== 'y' && key !== 'vx' && key !== 'vy' && key !== 'index'
          && key !== 'id' && key !== 'fx' && key !== 'fy' && key !== 'count' && key !== 'group') {
            node_details += `<p>${key}: ${d[key]}</p>`;
          }
        }
        node_details += '</div>';
        this.tooltip.html(node_details);
        return this.tooltip.style("visibility", "visible");})
      .on("mousemove", (event, d) =>{
        return this.tooltip.style("top", (event.pageY-350)+"px").style("left",(event.pageX-150)+"px");})
      .on("mouseout", (event, d) =>{return this.tooltip.style("visibility", "hidden");});

    // set the graph in motion
    this.force
      .nodes(this.nodes)
      .force('link').links(this.links, d => d.id);

      setTimeout(() =>{ this.force.alphaTarget(0.3).restart()}, 1000);
  }

  dragended(event, d) {
    if (!event.active) this.force.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }

  dragged(event, d) {
    d.fx = event.sourceEvent.layerX;
    d.fy = event.sourceEvent.layerY;
  }

  dragstarted(event, d) {
    if (!event.active) this.force.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }
}


