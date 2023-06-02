
	function brandOnChange() {
    var brands=[];
    $('.brand:checked').each(function(i){
      brands[i] = $(this).val();
    });

    console.log(brands);

    var price_start = 12;
    var price_end = 13;
   $.ajax({
       type: "GET",
       url: "/search_products",
       data: {'brand':brands, 'priceStart': price_start,'priceEnd': price_end},
       success: function (result) {
           $('#load_search_products').html('');
           $('#load_search_products').append(result.products_item_html);
       }
     });
}


	function sellerOnChange() {
    var sellers=[];
    $('.seller:checked').each(function(i){
      sellers[i] = $(this).val();
    });
    console.log(sellers);
    var price_start = 12;
    var price_end = 13;
   $.ajax({
       type: "GET",
       url: "/search_products",
       data: {'seller':sellers},
       success: function (result) {
       		console.log('asdf');
           $('#load_search_products').html('');
           $('#load_search_products').append(result.products_item_html);
       }
     });
}




function warrantyOnChange() {
    var warranties=[];
    $('.warranty:checked').each(function(i){
      warranties[i] = $(this).val();
    });
    console.log(warranties);
    var price_start = 12;
    var price_end = 13;
   $.ajax({
       type: "GET",
       url: "/search_products",
       data: {'warrenty':warranties},
       success: function (result) {
       		console.log('asdf');
           $('#load_search_products').html('');
           $('#load_search_products').append(result.products_item_html);
       }
     });
}