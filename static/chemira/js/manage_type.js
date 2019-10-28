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

            return [
                '<a class="remove" href="javascript:void(0)" title="删除">',
                '<i class="icon-remove text-danger"></i>',
                '</a>'
            ].join('');
    
    }


    function getApartNameSelections() {
        console.log("-----------")
        return $.map($table.bootstrapTable('getSelections'), function(row) {
            return row.lost_type_name;
        });
    }

    function getIdSelections() {
        return $.map($table.bootstrapTable('getSelections'), function(row) {
            return row.lost_type_id;
        });
    }


    $('#modifyUserPass').togglePassword({
        el: '#btn_show_pass'
    });

    window.operateEvents = {
        'click .modify': function(e, value, row, index) {
            console.log(row)
            var stu_obj = row;
            var lost_type_id = stu_obj.lost_type_id;
            var lost_type_name = stu_obj.lost_type_name;
            console.log(stu_obj.lost_type_name)
            $('#m_lost_type_id')[0].value = lost_type_id;
            $('#m_lost_type_name')[0].value = lost_type_name;
            $('#modifySingleUser').modal();
        },
        'click .remove': function(e, value, row, index) {
            // $('#deleteSingleRoom').modal();
            // $('#deleteSingleRoomMsg').html(row.lost_type_name + ' ?');
            // $('#deleteSingleRoomOk').click(function() {
                $.ajax({
                    url: "/remove_type/",
                    dataType: "json",
                    data: { "lost_type_ids": row.lost_type_id },
                    type: "POST",
                    success: function(msg) {
                            $table.bootstrapTable('remove', {
                                field: 'lost_type_id',
                                values: [row.lost_type_id]
                            });
                            $('#deleteSingleRoom').modal('hide');    
                    }
                });
            // });
        }
    };

    $remove.click(function() {
        var ids = getIdSelections();
        if (ids.length > 0) {
            //$('#deleteMultiRoom').modal();
            ids_str = ids.toString().trim();
            var stu_name = getApartNameSelections().toString().trim();
            //$('#deleteMultiRoomMsg').html( ' ?');
            //$('#deleteMultiRoomOk').click(function() {
                $.ajax({
                    url: "/remove_type/",
                    dataType: "json",
                    data: { lost_type_ids: ids_str },
                    type: "POST",
                    success: function(msg) {
                        window.location.reload();
                    }
                });
                $remove.prop('disabled', false);
                //$('#deleteMultiRoom').modal('hide');
            //});

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
        field: 'lost_type_id',
        title: '失物类型ID',
        align: 'center',
        valign: 'middle',
        sortable: true
    });
    columns.push({
        field: 'lost_type_name',
        title: '失物类型名称',
        align: 'center',
        valign: 'middle',
        sortable: true
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
        url: '/get_all_type',
        success: function(data) {
            var allRoomDataObjs = eval(data);
            $('#table').bootstrapTable('destroy').bootstrapTable({
                data: allRoomDataObjs,
                columns: columns
            });
        }
    });

    $('#datetimepicker1').datetimepicker({
        language: 'zh-CN'
    });
});
