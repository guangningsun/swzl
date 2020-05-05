<template>
    <view>
        <cu-custom bgColor="bg-gradual-blue" :isBack="true">
            <block slot="content">领取预登记</block>
        </cu-custom>
        <view class="cu-card case no-card margin-top">
            <view class="cu-item shadow">
                <view class="solid-bottom text-xl padding ">
                    <text class="text-dark-gray text-bold">请输入个人信息后到领取地址领取</text>
                </view>
            </view>
        </view>

        <form>
            <view class="cu-form-group">
                <view class="title">身份证号</view>
                <input placeholder="请输入证件号" name="input" v-model="id_card_number"/>
            </view>
            <view class="cu-form-group">
                <view class="title">姓名</view>
                <input placeholder="请输入姓名" name="input" v-model="owner_name"/>
            </view>
            <view class="cu-form-group">
                <view class="title">联系电话</view>
                <input placeholder="请输入电话号码" name="number" v-model="owner_tel"/>
            </view>
            <view class="cu-form-group align-start">
                <view class="title">特征描述</view>
                <textarea maxlength="-1" @input="itemDescInput" placeholder="物品物证描述"></textarea>
            </view>

            <!--身份证照上传-->
            <!--<view class="cu-bar bg-white margin-top">-->
            <!--<view class="action">-->
            <!--身份证照片上传-->
            <!--</view>-->
            <!--<view class="action">-->
            <!--{{imgList.length}}/1-->
            <!--</view>-->
            <!--</view>-->
            <!--<view class="cu-form-group">-->
            <!--<view class="grid col-4 grid-square flex-sub">-->
            <!--<view class="bg-img" v-for="(item,index) in imgList" :key="index" @tap="ViewImage" :data-url="imgList[index]">-->
            <!--<image :src="imgList[index]" mode="aspectFill"></image>-->
            <!--<view class="cu-tag bg-red" @tap.stop="DelImg" :data-index="index">-->
            <!--<text class='cuIcon-close'></text>-->
            <!--</view>-->
            <!--</view>-->
            <!--<view class="solids" @tap="ChooseImage" v-if="imgList.length<1">-->
            <!--<text class='cuIcon-cameraadd'></text>-->
            <!--</view>-->
            <!--</view>-->
            <!--</view>-->

        </form>

        <view class="padding flex flex-direction">
            <button class="cu-btn bg-gradual-green margin-tb-sm lg" @click="onSubmit" data-target="Modal">提交</button>
        </view>

        <view class="cu-modal" :class="modalName=='Modal'?'show':''">
            <view class="cu-dialog">
                <view class="cu-bar bg-white justify-end">
                    <view class="content">错误</view>
                    <view class="action" @tap="hideModal">
                        <text class="cuIcon-close text-red"></text>
                    </view>
                </view>
                <view class="padding-xl">
                    输入信息不正确，请检查。
                </view>
            </view>
        </view>

    </view>
</template>

<script>
    export default {
        data() {
            return {
                id_card_number: '',
                owner_name: '',
                owner_tel: '',
                itemDescValue: '',
                imgList: [],
                lost_detail: '',
                modalName: '内容非法',
            };
        },
        methods: {
            itemDescInput(e) {
                this.itemDescValue = e.detail.value
            },
            goToRegisterSuccess() {
                uni.navigateTo({
                    url: '../../pages/register/item_register_success'
                });
            },
            ChooseImage() {
                uni.chooseImage({
                    count: 1, //默认9
                    sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
                    sourceType: ['album'], //从相册选择
                    success: (res) => {
                        if (this.imgList.length != 0) {
                            this.imgList = this.imgList.concat(res.tempFilePaths)
                        } else {
                            this.imgList = res.tempFilePaths
                        }
                    }
                });
            },
            DelImg(e) {
                uni.showModal({
                    title: '删除',
                    content: '确定要删除图片吗？',
                    cancelText: '否',
                    confirmText: '是',
                    success: res => {
                        if (res.confirm) {
                            this.imgList.splice(e.currentTarget.dataset.index, 1)
                        }
                    }
                })
            },
            showModal(e) {
                this.modalName = e.currentTarget.dataset.target
            },
            hideModal(e) {
                this.modalName = null
            },
            onSubmit(e) {

                if (this.id_card_number == '' || this.id_card_number == undefined || this.id_card_number == null
                    || this.owner_name == '' || this.owner_name == undefined || this.owner_name == null
                    || this.owner_tel == '' || this.owner_tel == undefined || this.owner_tel == null) {
                    this.showModal(e);
                } else {
                    uni.request({
                        url: 'https://brilliantlife.com.cn:8002/web_modify_lost',
                        method: "POST",
                        dataType: 'json',
                        header: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        data: {
                            lost_id: this.lost_detail.lost_id,
                            received_name: this.owner_name,
                            received_id_card: this.id_card_number,
                            received_phone_number: this.owner_tel,
                            received_desc: this.itemDescValue

                        },
                        success: function (result) {
                            console.log(result);
                            uni.navigateTo({
                                url: '../../pages/register/item_register_success'
                            });
                        }
                    });
                }
            }
        },
        onShow() {
            this.lost_detail = uni.getStorageSync('key_lost_detail');
            this.lost_detail.lost_id
        }
    }
</script>


