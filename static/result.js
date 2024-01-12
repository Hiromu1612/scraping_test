'use strict';

$(function(){

/**
 * クリックイベント jQuery
 */
$('th').click(function(){
// 情報取得
let ele = $(this).attr('id');
let sortFlg = $(this).data('sort');

// リセット
$('th').data('sort', "");

// ソート順序
if(sortFlg == "" || sortFlg == "desc"){
    sortFlg = "asc";
    $(this).data('sort', "asc");
}else{
    sortFlg = "desc";
    $(this).data('sort', "desc");
}

// テーブルソート処理
sortTable(ele, sortFlg);
});

/**
 * テーブルソートメソッド javascript
 * 
 * @param ele 
 * @param sortFlg 
 */
function sortTable(ele, sortFlg){
let arr = $('table tbody tr').sort(function(a, b){
    // ソート対象が数値の場合
    if($.isNumeric($(a).find('td').eq(ele).text())){
    let aNum = Number($(a).find('td').eq(ele).text());
    let bNum = Number($(b).find('td').eq(ele).text());

    if(sortFlg == "asc"){
        return aNum - bNum;
    }else{
        return bNum - aNum;
    }
    }else{ // ソート対象が数値でない場合
    let sortNum = 1;

    // 比較時は小文字に統一
    if($(a).find('td').eq(ele).text().toLowerCase() > $(b).find('td').eq(ele).text().toLowerCase()){
        sortNum = 1;
    }else{
        sortNum = -1;
    }
    if(sortFlg == "desc"){
        sortNum *= (-1);
    }

    return sortNum;
    }
});
$('table tbody').html(arr);
}

});

$('.slider').slick({
    autoplay: true,//自動的に動き出すか。初期値はfalse。
    autoplaySpeed: 100,//次のスライドに切り替わる待ち時間
    infinite: true,//スライドをループさせるかどうか。初期値はtrue。
    speed: 400,//スライドのスピード。初期値は300。
    slidesToShow: 3,//スライドを画面に3枚見せる
    slidesToScroll: 1,//1回のスクロールで1枚の写真を移動して見せる
    prevArrow: '<div class="slick-prev"></div>',//矢印部分PreviewのHTMLを変更
    nextArrow: '<div class="slick-next"></div>',//矢印部分NextのHTMLを変更
    centerMode: true,//要素を中央ぞろえにする
    variableWidth: true,//幅の違う画像の高さを揃えて表示
    dots: true,//下部ドットナビゲーションの表示
});

