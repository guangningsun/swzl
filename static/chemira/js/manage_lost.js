// function onClickMultiDelete () {

//      $('#deleteMultiRoom').modal();
// }
var userName;
var domainCode;
var waterMode;

function onClickAddMultiRoom() {
    var floorNum = $('#floorNum')[0].value;
    var startNum = $('#startNum')[0].value;
    var endNum = $('#endNum')[0].value;
    var alphabet = $('#alphabet')[0].value;
    console.log(floorNum + ' ' + startNum + ' ' + endNum + ' ' + alphabet);
    $.ajax({
        type: "POST",
        url: "init_apartment.action",
        data: { "floor": floorNum, "start_num": startNum, "end_num": endNum, "domain_code": domainCode, "orderby": alphabet },
        success: function(msg) {
            console.log(msg);
            $('#addMultiRoom').modal('hide');
            location.reload();
        }
    });

}

function onDepositChange() {
    console.log($('#contract_month_price')[0].value);
    ($('#contract_deposit')[0].value) = $('#contract_month_price')[0].value;
}



$(document).ready(function() {


    var $table = $('#table'),
        $remove = $('#remove'),
        selections = [];

    function operateFormatter(value, row, index) {
        if (row.dev_status === "空闲") {
            return [
                '<a class="checkin" href="javascript:void(0)" title="登记">',
                '<i class="icon-plus-sign-alt text-primary"></i>',
                '</a>  ',
                '<a class="remove" href="javascript:void(0)" title="删除">',
                '<i class="icon-remove text-danger"></i>',
                '</a>'
            ].join('');
        } else {
            return [
                '<a class="modify" href="javascript:void(0)" title="修改">',
                '<i class="icon-pencil text-primary"></i>',
                '</a>  ',
                '<a class="remove" href="javascript:void(0)" title="删除">',
                '<i class="icon-remove text-danger"></i>',
                '</a>'
            ].join('');
        }

    }


    function getApartNameSelections() {
        return $.map($table.bootstrapTable('getSelections'), function(row) {
            return row.lost_id;
        });
    }

    function getIdSelections() {
        return $.map($table.bootstrapTable('getSelections'), function(row) {
            return row.lost_id;
        });
    }


    $('#modifyUserPass').togglePassword({
        el: '#btn_show_pass'
    });

    window.operateEvents = {
        'click .modify': function(e, value, row, index) {
            var stu_obj = row;
            console.log(stu_obj);
            var lost_id = stu_obj.lost_id;
            var pick_up_time = stu_obj.pick_up_time;
            //var bus_line_name = stu_obj.bus_line_name;
            var lost_type_name= stu_obj.lost_type_name;
            var receive_address = stu_obj.receive_address;
            //var is_received = stu_obj.is_received;
            var description = stu_obj.description;
            var received_name = stu_obj.received_name;
            var received_id_card = stu_obj.received_id_card;
            var received_phone_number = stu_obj.received_phone_number;
            var received_desc = stu_obj.received_desc;
            var contact_number = stu_obj.contact_number;

            $('#m_lost_id')[0].value = lost_id;
            $('#m_pick_up_time')[0].value = pick_up_time;
            //$('#m_bus_line_name')[0].value = bus_line_name;
            $('#m_lost_type_name')[0].value = lost_type_name;
            $('#m_receive_address')[0].value = receive_address;
            //$('#m_is_received')[0].value = is_received;
            $('#m_description')[0].value = description;
            $('#m_received_name')[0].value = received_name;
            $('#m_received_id_card')[0].value = received_id_card;
            $('#m_received_phone_number')[0].value = received_phone_number;
            $('#m_received_desc')[0].value = received_desc;
            $('#m_contact_number')[0].value = contact_number;

            $('#modifySingleLost').modal();
        },
        'click .remove': function(e, value, row, index) {
            console.log(row.lost_id);
            $('#deleteSingleRoom').modal();
            $('#deleteSingleRoomMsg').html(row.lost_id + ' ?');
            $('#deleteSingleRoomOk').click(function() {
                $.ajax({
                    url: "/remove_lost/",
                    dataType: "json",
                    data: { "lost_ids": row.lost_id },
                    type: "POST",
                    success: function(msg) {
                            $table.bootstrapTable('remove', {
                                field: 'lost_id',
                                values: [row.lost_id]
                            });
                            $('#deleteSingleRoom').modal('hide');    
                    }
                });
            });



        }
    };

    $remove.click(function() {
        var ids = getIdSelections();
        if (ids.length > 0) {
            $('#deleteMultiRoom').modal();
            ids_str = ids.toString().trim();
            var lost_id = getApartNameSelections().toString().trim();
            $('#deleteMultiRoomMsg').html(lost_id + ' ?');
            $('#deleteMultiRoomOk').click(function() {
                $.ajax({
                    url: "/remove_lost/",
                    dataType: "json",
                    data: { lost_ids: ids_str },
                    type: "POST",
                    success: function(msg) {
                        window.location.reload();
                    }
                });
                $remove.prop('disabled', false);
                $('#deleteMultiRoom').modal('hide');
            });

        }

    });

    $(window).resize(function() {
        $table.bootstrapTable('resetView', {
            // height: getHeight()
        });
    });

    function responseHandler(res) {
        console.log(res);
        $.each(res.rows, function(i, row) {
            row.state = $.inArray(row.stu_id, selections) !== -1;
        });
        return res;
    }

    var columns = [];

    columns.push({
        field: 'state',
        checkbox: true
    });
    columns.push({
        field: 'pick_up_time',
        title: '拾取时间',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'bus_line_name',
        title: '公交线路',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'lost_type_name',
        title: '失物类型',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'receive_address',
        title: '领取地址',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'description',
        title: '失物特征描述',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'contact_number',
        title: '联系电话',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'is_received',
        title: '是否已领取',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'received_name',
        title: '领取者姓名',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'received_id_card',
        title: '领取者身份证',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'received_phone_number',
        title: '领取者电话号',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'image_obj',
        title: '图片地址',
        align: 'center',
        valign: 'middle',
        sortable: true,
        width : '15%',
        formatter : function (value, row, index) {
                return "<img style='width: 50px;height: 50px;' src='/image_file/"+row['image_obj']+"' alt=''>"
        }
    });
    columns.push({
        field: 'operate',
        title: '操作',
        align: 'center',
        events: operateEvents,
        formatter: operateFormatter
    });

    $("#checkin_form").validation({
        reqmark: false,
        icon: false
    });




    $.ajax({
        type: "GET",
        url: '/get_all_lost',
        success: function(data) {
            var allRoomDataObjs = eval(data);
            $('#table').bootstrapTable('destroy').bootstrapTable({
                detailView : true,
                detailFormatter : function (index, row) {
                    var image = '<div class="photos">'
                    +'<a target="_blank" href="/image_file/'+row['image_obj']+'"><img alt="image" class="feed-photo" src="/image_file/'+row['image_obj']+'"></a>'
                    +'</div>';
                    return image;
                },
                data: allRoomDataObjs,
                columns: columns
            });
        }
    });

    $('#datetimepicker1').datetimepicker({
        language: 'zh-CN'
    });
});
