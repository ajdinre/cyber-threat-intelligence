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
  nodes = [
    {
      "country": "RU",
      "hostname": "gprs-client-83.149.9.216.misp.ru",
      "org": "AS31133 PJSC MegaFon",
      "city": "Moscow",
      "timezone": "Europe/Moscow",
      "latitude": "55.7522",
      "count": 9,
      "ip_address": "83.149.9.216",
      "postal": "127006",
      "region": "Moscow",
      "longitude": "37.6156",
      "group": 0,
      "name": "83.149.9.216"
  },
  {
      "country": "CZ",
      "org": "AS29208 Dial Telecom, a.s.",
      "city": "Prague",
      "timezone": "Europe/Prague",
      "latitude": "50.0880",
      "count": 1,
      "ip_address": "83.148.9.216",
      "postal": "110 00",
      "region": "Hlavní město Praha",
      "longitude": "14.4208",
      "group": 0,
      "name": "83.148.9.216"
  },
  {
      "country": "CN",
      "org": "AS4134 CHINANET-BACKBONE",
      "city": "Hangzhou",
      "timezone": "Asia/Shanghai",
      "latitude": "30.2936",
      "count": 1,
      "ip_address": "183.149.9.221",
      "region": "Zhejiang",
      "longitude": "120.1614",
      "group": 0,
      "name": "183.149.9.221"
  },
  {
      "country": "RU",
      "org": "AS31163 PJSC MegaFon",
      "city": "Krasnodar",
      "timezone": "Europe/Moscow",
      "latitude": "45.0448",
      "count": 1,
      "ip_address": "83.149.29.216",
      "postal": "350000",
      "region": "Krasnodarskiy",
      "longitude": "38.9760",
      "group": 0,
      "name": "83.149.29.216"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/images/kibana-dashboard.png",
      "httpVersion": "1.1",
      "sizeInBytes": "321631",
      "response": "200",
      "requestMethod": "GET",
      "community": 28,
      "timestamp": "17/May/2015:10:05:50",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/images/kibana-dashboard.png"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/images/frontend-response-codes.png",
      "httpVersion": "1.1",
      "sizeInBytes": "52878",
      "response": "200",
      "requestMethod": "GET",
      "community": 28,
      "timestamp": "17/May/2015:10:05:24",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/images/frontend-response-codes.png"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/css/fonts/Roboto-Regular.ttf",
      "httpVersion": "1.1",
      "sizeInBytes": "41820",
      "response": "200",
      "requestMethod": "GET",
      "community": 28,
      "timestamp": "17/May/2015:10:05:50",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/css/fonts/Roboto-Regular.ttf"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/css/fonts/Roboto-Bold.ttf",
      "httpVersion": "1.1",
      "sizeInBytes": "38720",
      "response": "200",
      "requestMethod": "GET",
      "community": 28,
      "timestamp": "17/May/2015:10:05:57",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/css/fonts/Roboto-Bold.ttf"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/images/sad-medic.png",
      "httpVersion": "1.1",
      "sizeInBytes": "430406",
      "response": "200",
      "requestMethod": "GET",
      "community": 28,
      "timestamp": "17/May/2015:10:05:34",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/images/sad-medic.png"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/plugin/notes/notes.js",
      "httpVersion": "1.1",
      "sizeInBytes": "2892",
      "response": "200",
      "requestMethod": "GET",
      "community": 28,
      "timestamp": "17/May/2015:10:05:07",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/plugin/notes/notes.js"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/plugin/zoom-js/zoom.js",
      "httpVersion": "1.1",
      "sizeInBytes": "7697",
      "response": "200",
      "requestMethod": "GET",
      "community": 0,
      "timestamp": "17/May/2015:10:05:12",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/plugin/zoom-js/zoom.js"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/plugin/highlight/highlight.js",
      "httpVersion": "1.1",
      "sizeInBytes": "26185",
      "response": "200",
      "requestMethod": "GET",
      "community": 0,
      "timestamp": "17/May/2015:10:05:47",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/plugin/highlight/highlight.js"
  },
  {
      "path": "/pre2sentations/logstash-monitorama-2013/images/kibana-dashboard3.png",
      "httpVersion": "1.1",
      "sizeInBytes": "171717",
      "response": "200",
      "requestMethod": "GET",
      "community": 28,
      "timestamp": "17/May/2015:10:05:43",
      "group": 1,
      "name": "/pre2sentations/logstash-monitorama-2013/images/kibana-dashboard3.png"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/images/kibana-search.png",
      "httpVersion": "1.1",
      "sizeInBytes": "203023",
      "response": "200",
      "requestMethod": "GET",
      "community": 27,
      "timestamp": "17/May/2015:10:05:03",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/images/kibana-search.png"
  },
  {
      "path": "/presentations/logstash-monitorama-2013/images/kibana-search.png",
      "httpVersion": "1.1",
      "sizeInBytes": "203023",
      "response": "200",
      "requestMethod": "GET",
      "community": 27,
      "timestamp": "17/May/2015:10:05:03",
      "group": 1,
      "name": "/presentations/logstash-monitorama-2013/images/kibana-search.png"
  }
  ];
  APIlinks = [
    [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/images/kibana-dashboard.png",
          "httpVersion": "1.1",
          "sizeInBytes": "321631",
          "response": "200",
          "requestMethod": "GET",
          "community": 28,
          "timestamp": "17/May/2015:10:05:50"
      }
  ],
  [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/images/frontend-response-codes.png",
          "httpVersion": "1.1",
          "sizeInBytes": "52878",
          "response": "200",
          "requestMethod": "GET",
          "community": 28,
          "timestamp": "17/May/2015:10:05:24"
      }
  ],
  [
      {
          "country": "CZ",
          "org": "AS29208 Dial Telecom, a.s.",
          "city": "Prague",
          "timezone": "Europe/Prague",
          "latitude": "50.0880",
          "count": 1,
          "ip_address": "83.148.9.216",
          "postal": "110 00",
          "region": "Hlavní město Praha",
          "longitude": "14.4208"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/css/fonts/Roboto-Regular.ttf",
          "httpVersion": "1.1",
          "sizeInBytes": "41820",
          "response": "200",
          "requestMethod": "GET",
          "community": 28,
          "timestamp": "17/May/2015:10:05:50"
      }
  ],
  [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/css/fonts/Roboto-Bold.ttf",
          "httpVersion": "1.1",
          "sizeInBytes": "38720",
          "response": "200",
          "requestMethod": "GET",
          "community": 28,
          "timestamp": "17/May/2015:10:05:57"
      }
  ],
  [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/images/sad-medic.png",
          "httpVersion": "1.1",
          "sizeInBytes": "430406",
          "response": "200",
          "requestMethod": "GET",
          "community": 28,
          "timestamp": "17/May/2015:10:05:34"
      }
  ],
  [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/plugin/notes/notes.js",
          "httpVersion": "1.1",
          "sizeInBytes": "2892",
          "response": "200",
          "requestMethod": "GET",
          "community": 28,
          "timestamp": "17/May/2015:10:05:07"
      }
  ],
  [
      {
          "country": "CN",
          "org": "AS4134 CHINANET-BACKBONE",
          "city": "Hangzhou",
          "timezone": "Asia/Shanghai",
          "latitude": "30.2936",
          "count": 1,
          "ip_address": "183.149.9.221",
          "region": "Zhejiang",
          "longitude": "120.1614"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/plugin/zoom-js/zoom.js",
          "httpVersion": "1.1",
          "sizeInBytes": "7697",
          "response": "200",
          "requestMethod": "GET",
          "community": 0,
          "timestamp": "17/May/2015:10:05:12"
      }
  ],
  [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/plugin/highlight/highlight.js",
          "httpVersion": "1.1",
          "sizeInBytes": "26185",
          "response": "200",
          "requestMethod": "GET",
          "community": 0,
          "timestamp": "17/May/2015:10:05:47"
      }
  ],
  [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/pre2sentations/logstash-monitorama-2013/images/kibana-dashboard3.png",
          "httpVersion": "1.1",
          "sizeInBytes": "171717",
          "response": "200",
          "requestMethod": "GET",
          "community": 28,
          "timestamp": "17/May/2015:10:05:43"
      }
  ],
  [
      {
          "country": "RU",
          "org": "AS31163 PJSC MegaFon",
          "city": "Krasnodar",
          "timezone": "Europe/Moscow",
          "latitude": "45.0448",
          "count": 1,
          "ip_address": "83.149.29.216",
          "postal": "350000",
          "region": "Krasnodarskiy",
          "longitude": "38.9760"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/images/kibana-search.png",
          "httpVersion": "1.1",
          "sizeInBytes": "203023",
          "response": "200",
          "requestMethod": "GET",
          "community": 27,
          "timestamp": "17/May/2015:10:05:03"
      }
  ],
  [
      {
          "country": "RU",
          "hostname": "gprs-client-83.149.9.216.misp.ru",
          "org": "AS31133 PJSC MegaFon",
          "city": "Moscow",
          "timezone": "Europe/Moscow",
          "latitude": "55.7522",
          "count": 9,
          "ip_address": "83.149.9.216",
          "postal": "127006",
          "region": "Moscow",
          "longitude": "37.6156"
      },
      "HAS_SENT",
      {
          "path": "/presentations/logstash-monitorama-2013/images/kibana-search.png",
          "httpVersion": "1.1",
          "sizeInBytes": "203023",
          "response": "200",
          "requestMethod": "GET",
          "community": 27,
          "timestamp": "17/May/2015:10:05:03"
      }
  ]
  ];

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
    this.fileService.getFilteredDataForMatTable(chosenServerNames, this.searchIpAddressesQuery)
      .subscribe((res)=>{
        console.log(res);
        this.dataSource = new MatTableDataSource(res);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      });


  }
  searchWithGrafana(){
    console.log("Search with Grafana Button Clicked!")
  }
  searchWithKibana(){
    console.log("Search with Kibana Button Clicked!")


}
  // d3 code
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
      .attr('width', '100%')
      .attr('height', '100%');

    this.force = d3.forceSimulation()
      .force('link', d3.forceLink().id((d: any) => d.name).distance(150))
      .force('charge', d3.forceManyBody().strength(-500))
      .force('x', d3.forceX(this.width / 2))
      .force('y', d3.forceY(this.height / 2))
      .on('tick', () => this.tick());


    // handles to link and node element groups
    this.path = this.svg.append('svg:g').selectAll('path');
    this.circle = this.svg.append('svg:g').selectAll('g');


    this.restart();
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
      .classed('selected', (d) => d === this.selectedLink)
      .merge(this.path);


    // circle (node) group
    // NB: the function arg is crucial here! nodes are known by name, not by index!
    this.circle = this.circle.data(this.nodes, (d) => d.name);

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
      });

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
        if(d.ip_address != null) { return d.name; }
        else { return ''; }
      })
    this.circle = g.merge(this.circle);

    //show tooltip
    this.circle
      .on('mouseover', (event, d) => {
        var node_details = '<div style="text-align: left;">';
        for (const key in d) {
          if(key !== 'x' && key !== 'y' && key !== 'vx' && key !== 'vy' && key !== 'index'
          && key !== 'name' && key !== 'fx' && key !== 'fy' && key !== 'count' && key !== 'group') {
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
      .force('link').links(this.links);

    this.force.alphaTarget(0.3).restart();
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


