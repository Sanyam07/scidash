webpackJsonp([22],{

/***/ 1036:
/***/ (function(module, exports, __webpack_require__) {

eval("var __WEBPACK_AMD_DEFINE_RESULT__;!(__WEBPACK_AMD_DEFINE_RESULT__ = function (require) {\n\n  var React = __webpack_require__(1);\n  var GEPPETTO = __webpack_require__(132);\n  __webpack_require__(1432);\n\n  $.widget.bridge('uitooltip', $.ui.tooltip);\n\n  var ToggleButton = React.createClass({\n    displayName: 'ToggleButton',\n\n    icon: null,\n    tooltip: null,\n    tooltipPosition: null,\n    label: null,\n    action: null,\n    attachTooltip: function attachTooltip() {\n      var self = this;\n      self.tooltipPosition = this.props.configuration.tooltipPosition;\n      if (self.tooltipPosition == null) {\n        self.tooltipPosition = { my: \"center bottom\", at: \"center top-10\" };\n      }\n      $(\"#\" + self.props.configuration.id).uitooltip({\n        position: self.tooltipPosition,\n        tooltipClass: \"tooltip-toggle\",\n        show: null, // show immediately\n        open: function open(event, ui) {\n          if (typeof event.originalEvent === 'undefined') {\n            return false;\n          }\n\n          var $id = $(ui.tooltip).attr('id');\n\n          // close any lingering tooltips\n          $('div.ui-tooltip').not('#' + $id).remove();\n        },\n        close: function close(event, ui) {\n          ui.tooltip.hover(function () {\n            $(this).stop(true).fadeTo(400, 1);\n          }, function () {\n            $(this).fadeOut('400', function () {\n              $(this).remove();\n            });\n          });\n        },\n        content: function content() {\n          return self.state.tooltip;\n        }\n      });\n    },\n\n    getInitialState: function getInitialState() {\n      return {\n        icon: this.icon,\n        label: this.label,\n        tooltip: this.tooltip,\n        action: this.action,\n        disabled: false\n      };\n    },\n\n    componentDidMount: function componentDidMount() {\n      this.attachTooltip();\n      this.evaluateState();\n\n      // attach handlers if any\n      if (this.props.configuration.eventHandler != undefined) {\n        this.props.configuration.eventHandler(this);\n      }\n    },\n\n    clickEvent: function clickEvent() {\n      this.evaluateState();\n      // there may or may not be a dynamic action to be executed via console\n      if (this.action != '') {\n        GEPPETTO.CommandController.execute(this.action, true);\n      }\n      if (this.props.configuration.clickHandler != undefined) {\n        this.props.configuration.clickHandler(this.props.id);\n      }\n      $('div.ui-tooltip').remove();\n    },\n\n    showToolTip: function showToolTip() {\n      var self = this;\n      var selfSelector = $(\"#\" + self.props.configuration.id);\n      selfSelector.uitooltip({ content: self.state.tooltip, position: { my: \"right center\", at: \"left center\" } });\n      selfSelector.mouseover().delay(2000).queue(function () {\n        $(this).mouseout().dequeue();\n      });\n    },\n\n    evaluateState: function evaluateState() {\n      // figure out if disabled\n      var disableBtn = this.props.disabled;\n      if (disableBtn == undefined) {\n        // fall back on disableCondition from config if any\n        var disableCondition = this.props.configuration.disableCondition;\n        if (disableCondition != '' && disableCondition != undefined) {\n          disableCondition = disableCondition.replace(/['\"]+/g, '');\n          disableBtn = eval(disableCondition);\n        }\n      }\n\n      // figure out if hidden\n      var hideBtn = this.props.hidden;\n      if (hideBtn == undefined) {\n        // fall back on disableCondition from config if any\n        var hideCondition = this.props.configuration.hideCondition;\n        if (hideCondition != '' && hideCondition != undefined) {\n          hideCondition = hideCondition.replace(/['\"]+/g, '');\n          hideBtn = eval(hideCondition);\n        }\n      }\n\n      // condition could be function or string\n      var condition = this.props.configuration.condition;\n      var conditionResult = false;\n      if (typeof condition === 'function') {\n        conditionResult = condition();\n      } else {\n        if (condition != '') {\n          condition = condition.replace(/['\"]+/g, '');\n          conditionResult = eval(condition);\n        }\n      }\n\n      if (!conditionResult) {\n        this.icon = this.props.configuration.false.icon;\n        this.action = this.props.configuration.false.action;\n        this.label = this.props.configuration.false.label;\n        this.tooltip = this.props.configuration.false.tooltip;\n      } else {\n        this.icon = this.props.configuration.true.icon;\n        this.action = this.props.configuration.true.action;\n        this.label = this.props.configuration.true.label;\n        this.tooltip = this.props.configuration.true.tooltip;\n      }\n\n      if (this.isMounted()) {\n        this.setState({ toggled: conditionResult, icon: this.icon, action: this.action, label: this.label, tooltip: this.tooltip, disabled: disableBtn, hidden: hideBtn });\n      }\n    },\n\n    render: function render() {\n      // build css for button\n      var cssClass = this.props.configuration.id + \" btn pull-right\";\n\n      // figure out if toggled to reflect visually with css class\n      var toggled = false;\n      if (this.props.toggled != undefined && typeof this.props.toggled === \"boolean\") {\n        // if prop is passed ignore state, prop overrides precedence\n        // NOTE: this lets the component be controlled from a parent with props\n        toggled = this.props.toggled;\n      } else {\n        // fallback on internally kept state\n        toggled = this.state.toggled;\n      }\n\n      if (toggled) {\n        cssClass += \" toggle-button-toggled\";\n      }\n\n      // check if the button is being hidden from he parent via prop\n      if (this.props.hidden === true) {\n        cssClass += \" toggle-button-hidden\";\n      }\n\n      return React.createElement(\n        'div',\n        { className: 'toggleButton' },\n        React.createElement(\n          'button',\n          { id: this.props.configuration.id, className: cssClass, type: 'button', title: '',\n            rel: 'tooltip', onClick: this.clickEvent, disabled: this.props.disabled === true || this.state.disabled === true },\n          React.createElement('i', { className: this.state.icon }),\n          this.state.label\n        )\n      );\n    }\n  });\n\n  return ToggleButton;\n}.call(exports, __webpack_require__, exports, module),\n\t\t\t\t__WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__));\n\n//////////////////\n// WEBPACK FOOTER\n// ./js/components/controls/toggleButton/ToggleButton.js\n// module id = 1036\n// module chunks = 2 22\n\n//# sourceURL=webpack:///./js/components/controls/toggleButton/ToggleButton.js?");

/***/ }),

/***/ 1432:
/***/ (function(module, exports, __webpack_require__) {

eval("// style-loader: Adds some css to the DOM by adding a <style> tag\n\n// load the styles\nvar content = __webpack_require__(1433);\nif(typeof content === 'string') content = [[module.i, content, '']];\n// add the styles to the DOM\nvar update = __webpack_require__(25)(content, {});\nif(content.locals) module.exports = content.locals;\n// Hot Module Replacement\nif(false) {\n\t// When the styles change, update the <style> tags\n\tif(!content.locals) {\n\t\tmodule.hot.accept(\"!!../../../../node_modules/css-loader/index.js!../../../../node_modules/less-loader/dist/cjs.js?{\\\"modifyVars\\\":{\\\"url\\\":\\\"'../../../extensions/geppetto-default/colors'\\\"}}!./ToggleButton.less\", function() {\n\t\t\tvar newContent = require(\"!!../../../../node_modules/css-loader/index.js!../../../../node_modules/less-loader/dist/cjs.js?{\\\"modifyVars\\\":{\\\"url\\\":\\\"'../../../extensions/geppetto-default/colors'\\\"}}!./ToggleButton.less\");\n\t\t\tif(typeof newContent === 'string') newContent = [[module.id, newContent, '']];\n\t\t\tupdate(newContent);\n\t\t});\n\t}\n\t// When the module is disposed, remove the <style> tags\n\tmodule.hot.dispose(function() { update(); });\n}\n\n//////////////////\n// WEBPACK FOOTER\n// ./js/components/controls/toggleButton/ToggleButton.less\n// module id = 1432\n// module chunks = 2 22\n\n//# sourceURL=webpack:///./js/components/controls/toggleButton/ToggleButton.less?");

/***/ }),

/***/ 1433:
/***/ (function(module, exports, __webpack_require__) {

eval("exports = module.exports = __webpack_require__(24)(undefined);\n// imports\n\n\n// module\nexports.push([module.i, \".dark-orange {\\n  color: #fc401a;\\n}\\n.orange {\\n  color: #fc6320;\\n}\\n.orange-color {\\n  color: #fc6320;\\n}\\n.orange-color-bg {\\n  background-color: #fc6320;\\n}\\n.toggle-button-toggled {\\n  color: white !important;\\n  background: #fc6320 !important;\\n}\\n.toggle-button-hidden {\\n  display: none;\\n}\\n.tooltip-toggle {\\n  height: 25px;\\n  max-width: 800px;\\n  border-radius: 5px;\\n  border: 1px solid black;\\n  padding: 2px 4px 2px 4px;\\n  background: white;\\n  opacity: 1;\\n  left: 200px;\\n}\\n\", \"\"]);\n\n// exports\n\n\n//////////////////\n// WEBPACK FOOTER\n// ./node_modules/css-loader!./node_modules/less-loader/dist/cjs.js?{\"modifyVars\":{\"url\":\"'../../../extensions/geppetto-default/colors'\"}}!./js/components/controls/toggleButton/ToggleButton.less\n// module id = 1433\n// module chunks = 2 22\n\n//# sourceURL=webpack:///./js/components/controls/toggleButton/ToggleButton.less?./node_modules/css-loader!./node_modules/less-loader/dist/cjs.js?%7B%22modifyVars%22:%7B%22url%22:%22'../../../extensions/geppetto-default/colors'%22%7D%7D");

/***/ })

});