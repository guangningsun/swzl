<template>
    <view>
        <cu-custom bgColor="bg-gradual-blue" :isBack="true">
            <block slot="content">滨海公交失物招领</block>
        </cu-custom>

        <view class="margin-top solid-bottom ">
            <view class="cu-card article" v-for="(item,index) in lost_result_data" :key="index">
                <view class="cu-item shadow">
                    <view class="content">
                        <image class="bg-gray margin-top-sm shadow shadow-lg" :src='"https://brilliantlife.com.cn:8002/image_file/" + item.image_obj'
                               mode="aspectFill"></image>
                        <view class="desc padding-top-sm">

                            <view class="flex justify-start">
                                <view class="margin-xs text-gray">类型:</view>
                                <view class="margin-xs">{{item.lost_type_name}}</view>
                            </view>

                            <view class="flex justify-start">
                                <view class="margin-xs text-gray">时间:</view>
                                <view class="margin-xs ">{{item.pick_up_time}}</view>
                            </view>

                            <view class="flex justify-start">
                                <view class="margin-xs text-gray">路线:</view>
                                <view class="margin-xs">{{item.bus_line_name}}</view>
                            </view>

                            <view class="flex justify-end">
                                <button class="cu-btn round lines-green" @click="onConfirm(item)">确认并领取</button>
                            </view>
                        </view>
                    </view>
                </view>
            </view>
        </view>
    </view>

    </view>
</template>

<script>
    export default {
        data() {
            return {
                lost_result_data:''
            };
        },
        methods: {
            goToDetail(){
                uni.navigateTo({
                    url: '../../pages/detail/item_detail'
                });
            },
            onConfirm: function (e) {
                uni.setStorageSync("key_lost_detail", e);
                this.goToDetail();
            }
        },
        onShow() {
            this.lost_result_data = uni.getStorageSync('key_lost_result');
            console.log(this.lost_result_data);

        }
    }
</script>


