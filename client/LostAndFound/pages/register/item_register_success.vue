<template>
    <view>
        <cu-custom bgColor="bg-gradual-blue" :isBack="false">
            <block slot="content">领取预登记成功</block>
        </cu-custom>
        <view>
            <view class="flex-sub text-center bg-white">
                <view class="text-xsl padding">
                    <text class="text-green cuIcon-roundcheckfill" ></text>
                </view>
            </view>
            <view class="cu-form-group">
                <view class="title">领取地址</view>
                <view>{{item_address}}</view>
            </view>
            <view class="cu-form-group">
                <view class="title">联系方式</view>
                <view>{{tel}}</view>
            </view>
        </view>
    </view>
</template>

<script>
    export default {
        data() {
            return {
                item_address:'',
                tel:'',
            };
        },
        onShow() {
            this.lost_detail = uni.getStorageSync('key_lost_detail');
            this.item_address = this.lost_detail.receive_address;
            this.tel = this.lost_detail.contact_number;
        }
    }
</script>


