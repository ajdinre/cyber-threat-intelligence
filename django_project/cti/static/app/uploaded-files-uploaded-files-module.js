(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["uploaded-files-uploaded-files-module"],{

/***/ "Wj56":
/*!*****************************************************************!*\
  !*** ./src/app/uploaded-files/uploaded-files-routing.module.ts ***!
  \*****************************************************************/
/*! exports provided: UploadedFilesRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UploadedFilesRoutingModule", function() { return UploadedFilesRoutingModule; });
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/router */ "tyNb");
/* harmony import */ var _uploaded_files_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./uploaded-files.component */ "wKSu");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");




const routes = [
    {
        path: '',
        pathMatch: 'full',
        component: _uploaded_files_component__WEBPACK_IMPORTED_MODULE_1__["UploadedFilesComponent"]
    }
];
class UploadedFilesRoutingModule {
}
UploadedFilesRoutingModule.ɵfac = function UploadedFilesRoutingModule_Factory(t) { return new (t || UploadedFilesRoutingModule)(); };
UploadedFilesRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: UploadedFilesRoutingModule });
UploadedFilesRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ imports: [[_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)], _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](UploadedFilesRoutingModule, { imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]], exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] }); })();


/***/ }),

/***/ "w56C":
/*!*********************************************************!*\
  !*** ./src/app/uploaded-files/uploaded-files.module.ts ***!
  \*********************************************************/
/*! exports provided: UploadedFilesModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UploadedFilesModule", function() { return UploadedFilesModule; });
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/common */ "ofXK");
/* harmony import */ var _uploaded_files_routing_module__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./uploaded-files-routing.module */ "Wj56");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");



class UploadedFilesModule {
}
UploadedFilesModule.ɵfac = function UploadedFilesModule_Factory(t) { return new (t || UploadedFilesModule)(); };
UploadedFilesModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: UploadedFilesModule });
UploadedFilesModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ imports: [[
            _angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"],
            _uploaded_files_routing_module__WEBPACK_IMPORTED_MODULE_1__["UploadedFilesRoutingModule"]
        ]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](UploadedFilesModule, { imports: [_angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"],
        _uploaded_files_routing_module__WEBPACK_IMPORTED_MODULE_1__["UploadedFilesRoutingModule"]] }); })();


/***/ })

}]);
//# sourceMappingURL=uploaded-files-uploaded-files-module.js.map