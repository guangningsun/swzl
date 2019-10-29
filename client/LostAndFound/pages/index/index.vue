<template>
    <view>
        <cu-custom bgColor="bg-gradual-blue" :isBack="false">
            <block slot="content">滨海公交失物招领</block>
        </cu-custom>
        <view class="cu-card case no-card">
            <view class="cu-item shadow">
                <view class="image">
                    <image src="../../static/binghaitranslogo.png" mode="widthFix"></image>
                </view>
            </view>
        </view>
        <view class="cu-form-group margin-top">
            <view class="title">日期选择</view>
            <picker mode="date" :value="date" start="2015-09-01" end="2020-09-01" @change="dateChange">
                <view class="picker">
                    {{date}}
                </view>
            </picker>
        </view>
        <view class="cu-form-group ">
            <view class="title">时间选择</view>
            <picker mode="time" :value="time" start="00:01" end="23:59" @change="timeChange">
                <view class="picker">
                    {{time}}
                </view>
            </picker>
        </view>
        <view class="cu-form-group">
            <view class="title">请选择路线</view>
            <picker @change="busRoutePickerChange" :value="route_picker_index" :range="bus_route_picker">
                <view class="picker">
                    {{route_picker_index>-1 ? bus_route_picker[route_picker_index]:'选择公交线路'}}
                </view>
            </picker>
        </view>
        <view class="cu-form-group">
            <view class="title">请物品类型</view>
            <picker @change="typePickerChange" :value="type_picker_index" :range="type_picker">
                <view class="picker">
                    {{type_picker_index>-1 ? type_picker[type_picker_index]:'选择物品类型'}}
                </view>
            </picker>
        </view>

        <view class="padding flex flex-direction">
            <button class="cu-btn bg-gradual-green margin-tb-sm lg" :disabled = "btn_disabled" @click="onSubmit">提交</button>
        </view>

    </view>
</template>

<script>
    export default {
        data() {
            return {
                route_picker_index: -1,
                type_picker_index: -1,
                time: '12:00',
                date: '2018-12-25',
                bus_route_picker: [],
                type_picker: [],
                btn_disabled: true
            };
        },
        methods: {
            timeChange(e) {
                this.time = e.detail.value;
                this.checkBtnEnable();
            },
            dateChange(e) {
                this.date = e.detail.value;
                this.checkBtnEnable();
            },
            busRoutePickerChange(e) {
                this.route_picker_index = e.detail.value;
                this.checkBtnEnable();
            },
            typePickerChange(e) {
                this.type_picker_index = e.detail.value;
                this.checkBtnEnable();
            },
            itemDescInput(e) {
                this.itemDescValue = e.detail.value;
            },
            goToResultList() {
                uni.navigateTo({
                    url: '../../pages/result/item_result'
                });
            },
            requestBusRoute() {
                var bus_list = this.bus_route_picker;
                uni.request({
                    url: 'http://114.115.136.120:8002/get_all_bus_line',
                    method: "POST",
                    dataType: 'json',
                    header: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    success: res => {
                        res.data.map(function (item) {
                            bus_list.push(item.bus_line_name)
                        });
                    },
                    fail: (err) => {
                        console.log('request bus line fail', err);
                    },
                    complete: () => {
                    }
                });
            },
            requestLostType() {
                var lostTypeList = this.type_picker;
                uni.request({
                    url: 'http://114.115.136.120:8002/get_all_type',
                    method: "POST",
                    dataType: 'json',
                    header: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    success: res => {
                        res.data.map(function (item) {
                            lostTypeList.push(item.lost_type_name)
                        });
                    },
                    fail: (err) => {
                        console.log('request get_all_type fail', err);
                    },
                    complete: () => {
                    }
                });
            },
            getTodayDate() {
                var date = new Date();
                var seperator = "-";
                var year = date.getFullYear();
                var month = date.getMonth() + 1;
                var strDate = date.getDate();
                if (month >= 1 && month <= 9) {
                    month = "0" + month;
                }
                if (strDate >= 0 && strDate <= 9) {
                    strDate = "0" + strDate;
                }
                return year + seperator + month + seperator + strDate;
            },
            getNowTime() {
                let date = new Date();
                let h = date.getHours();
                h = h < 10 ? ('0' + h) : h;
                let m = date.getMinutes();
                m = m < 10 ? ('0' + m) : m;
                return h + ':' + m;
            },
            checkBtnEnable() {
                if (this.date == ''
                    || this.bus_route_picker[this.route_picker_index] == ''
                    || this.bus_route_picker[this.route_picker_index] == undefined
                    || this.type_picker[this.type_picker_index] == ''
                    || this.type_picker[this.type_picker_index] == undefined) {
                    this.btn_disabled = true;
                } else {
                    this.btn_disabled = false;
                }
            },
            onSubmit() {
                var date = this.date;
                var type_name = '';
                var bus_line_name = '';

                if (this.type_picker[this.type_picker_index] !== undefined) {
                    type_name = this.type_picker[this.type_picker_index];
                }

                if (this.bus_route_picker[this.route_picker_index] !== undefined) {
                    bus_line_name = this.bus_route_picker[this.route_picker_index];
                }

                console.log("date:" + date);
                console.log("type:" + type_name);
                console.log("bus_line_name:" + bus_line_name);

                uni.request({
                    url: 'http://114.115.136.120:8002/get_lost_by_bus_line',
                    method: "POST",
                    dataType: 'json',
                    header: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    data: {
                        search_date: date,
                        lost_type_name: type_name,
                        bus_line_name: bus_line_name
                    },
                    success: res => {
                        var result = res.data;
                        console.log(result);
                        if (result.length > 0) {
                            this.goToResultList();
                            uni.setStorageSync("key_lost_result", result);
                        }
                        else {
                            console.log('no result')
                            uni.showToast({
                                title: '无查找结果',
                                icon: "none",
                                mask: !1
                            })
                        }
                    }
                });
            }
        },
        onShow() {
            this.requestBusRoute();
            this.requestLostType();

            this.date = this.getTodayDate();
            this.time = this.getNowTime();
        }
    }
</script>


