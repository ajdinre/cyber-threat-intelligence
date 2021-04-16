import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FileSearchTableComponent } from './file-search-table.component';

describe('FileSearchTableComponent', () => {
  let component: FileSearchTableComponent;
  let fixture: ComponentFixture<FileSearchTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FileSearchTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FileSearchTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
