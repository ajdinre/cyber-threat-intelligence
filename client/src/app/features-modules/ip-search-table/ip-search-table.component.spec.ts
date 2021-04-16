import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IpSearchTableComponent } from './ip-search-table.component';

describe('IpSearchTableComponent', () => {
  let component: IpSearchTableComponent;
  let fixture: ComponentFixture<IpSearchTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IpSearchTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IpSearchTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
