(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-register-item_register"],{3857:function(t,e,i){"use strict";i.r(e);var n=i("9e7f"),a=i("d5a6");for(var s in a)"default"!==s&&function(t){i.d(e,t,(function(){return a[t]}))}(s);var o,l=i("f0c5"),c=Object(l["a"])(a["default"],n["b"],n["c"],!1,null,null,null,!1,n["a"],o);e["default"]=c.exports},5422:function(t,e,i){"use strict";(function(t){i("99af"),i("a434"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var n={data:function(){return{owner_name:"",owner_tel:"",itemDescValue:"",imgList:[],lost_detail:"",modalName:"内容非法"}},methods:{itemDescInput:function(t){this.itemDescValue=t.detail.value},goToRegisterSuccess:function(){uni.navigateTo({url:"../../pages/register/item_register_success"})},ChooseImage:function(){var t=this;uni.chooseImage({count:1,sizeType:["original","compressed"],sourceType:["album"],success:function(e){0!=t.imgList.length?t.imgList=t.imgList.concat(e.tempFilePaths):t.imgList=e.tempFilePaths}})},DelImg:function(t){var e=this;uni.showModal({title:"删除",content:"确定要删除图片吗？",cancelText:"否",confirmText:"是",success:function(i){i.confirm&&e.imgList.splice(t.currentTarget.dataset.index,1)}})},showModal:function(t){this.modalName=t.currentTarget.dataset.target},hideModal:function(t){this.modalName=null},onSubmit:function(e){""==this.owner_name||void 0==this.owner_name||null==this.owner_name||""==this.owner_tel||void 0==this.owner_tel||null==this.owner_tel?this.showModal(e):uni.request({url:"https://brilliantlife.com.cn:8002/web_modify_lost",method:"POST",dataType:"json",header:{"Content-Type":"application/x-www-form-urlencoded"},data:{lost_id:this.lost_detail.lost_id,received_name:this.owner_name,received_id_card:this.id_card_number,received_phone_number:this.owner_tel,received_desc:this.itemDescValue},success:function(e){t("log",e," at pages/register/item_register.vue:150"),uni.navigateTo({url:"../../pages/register/item_register_success"})}})}},onShow:function(){this.lost_detail=uni.getStorageSync("key_lost_detail"),this.lost_detail.lost_id}};e.default=n}).call(this,i("0de9")["log"])},"9e7f":function(t,e,i){"use strict";var n,a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",[i("cu-custom",{attrs:{bgColor:"bg-gradual-blue",isBack:!0}},[i("template",{attrs:{slot:"content"},slot:"content"},[t._v("领取预登记")])],2),i("v-uni-view",{staticClass:"cu-card case no-card margin-top"},[i("v-uni-view",{staticClass:"cu-item shadow"},[i("v-uni-view",{staticClass:"solid-bottom text-xl padding "},[i("v-uni-text",{staticClass:"text-dark-gray text-bold"},[t._v("请输入个人信息后到领取地址领取")])],1)],1)],1),i("v-uni-form",[i("v-uni-view",{staticClass:"cu-form-group"},[i("v-uni-view",{staticClass:"title"},[t._v("姓名")]),i("v-uni-input",{attrs:{placeholder:"请输入姓名",name:"input"},model:{value:t.owner_name,callback:function(e){t.owner_name=e},expression:"owner_name"}})],1),i("v-uni-view",{staticClass:"cu-form-group"},[i("v-uni-view",{staticClass:"title"},[t._v("联系电话")]),i("v-uni-input",{attrs:{placeholder:"请输入电话号码",name:"number"},model:{value:t.owner_tel,callback:function(e){t.owner_tel=e},expression:"owner_tel"}})],1),i("v-uni-view",{staticClass:"cu-form-group align-start"},[i("v-uni-view",{staticClass:"title"},[t._v("特征描述")]),i("v-uni-textarea",{attrs:{maxlength:"-1",placeholder:"物品物证描述"},on:{input:function(e){arguments[0]=e=t.$handleEvent(e),t.itemDescInput.apply(void 0,arguments)}}})],1)],1),i("v-uni-view",{staticClass:"padding flex flex-direction"},[i("v-uni-button",{staticClass:"cu-btn bg-gradual-green margin-tb-sm lg",attrs:{"data-target":"Modal"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.onSubmit.apply(void 0,arguments)}}},[t._v("提交")])],1),i("v-uni-view",{staticClass:"cu-modal",class:"Modal"==t.modalName?"show":""},[i("v-uni-view",{staticClass:"cu-dialog"},[i("v-uni-view",{staticClass:"cu-bar bg-white justify-end"},[i("v-uni-view",{staticClass:"content"},[t._v("错误")]),i("v-uni-view",{staticClass:"action",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.hideModal.apply(void 0,arguments)}}},[i("v-uni-text",{staticClass:"cuIcon-close text-red"})],1)],1),i("v-uni-view",{staticClass:"padding-xl"},[t._v("输入信息不正确，请检查。")])],1)],1)],1)},s=[];i.d(e,"b",(function(){return a})),i.d(e,"c",(function(){return s})),i.d(e,"a",(function(){return n}))},d5a6:function(t,e,i){"use strict";i.r(e);var n=i("5422"),a=i.n(n);for(var s in n)"default"!==s&&function(t){i.d(e,t,(function(){return n[t]}))}(s);e["default"]=a.a}}]);