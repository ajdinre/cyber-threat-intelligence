(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["analyse-analyse-module"],{

/***/ "KmNi":
/*!*******************************************!*\
  !*** ./src/app/analyse/analyse.module.ts ***!
  \*******************************************/
/*! exports provided: AnalyseModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AnalyseModule", function() { return AnalyseModule; });
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/common */ "ofXK");
/* harmony import */ var _analyse_routing_module__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./analyse-routing.module */ "cS+G");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");



class AnalyseModule {
}
AnalyseModule.ɵfac = function AnalyseModule_Factory(t) { return new (t || AnalyseModule)(); };
AnalyseModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: AnalyseModule });
AnalyseModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ imports: [[
            _angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"],
            _analyse_routing_module__WEBPACK_IMPORTED_MODULE_1__["AnalyseRoutingModule"]
        ]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](AnalyseModule, { imports: [_angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"],
        _analyse_routing_module__WEBPACK_IMPORTED_MODULE_1__["AnalyseRoutingModule"]] }); })();


/***/ }),

/***/ "Vnoy":
/*!**********************************************!*\
  !*** ./src/app/analyse/analyse.component.ts ***!
  \**********************************************/
/*! exports provided: AnalyseComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AnalyseComponent", function() { return AnalyseComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");

class AnalyseComponent {
    constructor() { }
    ngOnInit() {
    }
}
AnalyseComponent.ɵfac = function AnalyseComponent_Factory(t) { return new (t || AnalyseComponent)(); };
AnalyseComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: AnalyseComponent, selectors: [["app-analyse"]], decls: 2, vars: 0, template: function AnalyseComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, "analyse works!");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } }, styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJhbmFseXNlLmNvbXBvbmVudC5jc3MifQ== */"] });


/***/ }),

/***/ "cS+G":
/*!***************************************************!*\
  !*** ./src/app/analyse/analyse-routing.module.ts ***!
  \***************************************************/
/*! exports provided: AnalyseRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AnalyseRoutingModule", function() { return AnalyseRoutingModule; });
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/router */ "tyNb");
/* harmony import */ var _analyse_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./analyse.component */ "Vnoy");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");




const routes = [
    {
        path: '',
        pathMatch: 'full',
        component: _analyse_component__WEBPACK_IMPORTED_MODULE_1__["AnalyseComponent"]
    }
];
class AnalyseRoutingModule {
}
AnalyseRoutingModule.ɵfac = function AnalyseRoutingModule_Factory(t) { return new (t || AnalyseRoutingModule)(); };
AnalyseRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: AnalyseRoutingModule });
AnalyseRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ imports: [[_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)], _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](AnalyseRoutingModule, { imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]], exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] }); })();


/***/ })

}]);
//# sourceMappingURL=analyse-analyse-module.js.map