<template>
    <view>
        <cu-custom bgColor="bg-gradual-blue" :isBack="true">
            <block slot="content">滨海公交失物招领</block>
        </cu-custom>
        <view class="cu-card case no-card margin-top">
            <view class="cu-item shadow">
                <view class="image">
                    <!--<image src="../../static/binghaitranslogo.png" mode="widthFix"></image>-->
                    <image :src="image" mode="widthFix"></image>
                </view>
            </view>
        </view>
        <view class="cu-form-group">
            <view class="title">拾获时间</view>
            <view>{{time}}</view>
        </view>
        <view class="cu-form-group">
            <view class="title">拾获路线</view>
            <view>{{bus_route}}</view>
        </view>
        <view class="cu-form-group">
            <view class="title">失物种类</view>
            <view>{{item_type}}</view>
        </view>
        <view class="cu-form-group">
            <view class="title">领取地址</view>
            <view>{{item_address}}</view>
        </view>
        <view class="cu-form-group">
            <view class="title">联系方式</view>
            <view>{{tel}}</view>
        </view>
        <view class="cu-form-group">
            <view class="title">特征描述</view>
            <view>{{item_desc}}</view>
        </view>

        <view class="padding flex flex-direction">
            <button class="cu-btn bg-gradual-green margin-tb-sm lg" @click="onItemConfirm">失物确认</button>
        </view>

    </view>
</template>

<script>
    export default {
        data() {
            return {
                lost_detail:'',
                time: '',
                bus_route: '',
                item_type: '',
                item_address:'',
                item_desc: '',
                tel:'',
                image:''
            };
        },
        methods: {
            goToRegister() {
                uni.navigateTo({
                    url: '../../pages/register/item_register'
                });
            },
            onItemConfirm() {
                this.goToRegister();
            }
        },
        onShow() {
            this.lost_detail = uni.getStorageSync('key_lost_detail');
            this.time = this.lost_detail.pick_up_time;
            this.bus_route = this.lost_detail.bus_line_name;
            this.item_type = this.lost_detail.lost_type_name;
            this.item_address = this.lost_detail.receive_address;
            this.item_desc = this.lost_detail.received_desc;
            this.tel = this.lost_detail.contact_number;
            this.image = "http://114.115.136.120:8002/image_file/" + this.lost_detail.image_obj;
        }
    }
</script>


