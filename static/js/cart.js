
// ===================increase cart items=================

$('.plus-cart').click(function(){
    var id=$(this).attr('pid').toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type : "GET",
        url :"/pluscart",
        data : {
            prod_id : id
        },
        success : function(data){
            eml.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
        }
    })

})

// ===========================decrease cart items===========================

$('.minus-cart').click(function(){
    var id=$(this).attr('pid').toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type : "GET",
        url :"/minuscart",
        data : {
            prod_id : id
        },
        success : function(data){
            eml.innerText = data.quantity
            document.getElementById('amount').innerText = data.amount
            document.getElementById('totalamount').innerText = data.totalamount
        }
    })

})

// =====================Remove cart item======================

$('.remove-cart').click(function(){
    var id=$(this).attr('pid').toString();
    var eml = this
    $.ajax({
        type : "GET",
        url :"/removecart",
        data : {
            prod_id : id
        },
        success : function(data){
            if (data.cart == true){
                console.log(data.cart)
                eml.innerText = data.quantity
                document.getElementById('amount').innerText = data.amount
                document.getElementById('totalamount').innerText = data.totalamount
                eml.parentNode.parentNode.parentNode.parentNode.remove()
            } else {
                console.log(data.cart)
                eml.parentNode.parentNode.parentNode.parentNode.remove()
            }
        }
    })
})


// =============== Wishlist==================

$('.plus-wishlist').click(function(){
    var id=$(this).attr('pid').toString();
    $.ajax({
        type :'GET',
        url : '/pluswishlist',
        data : {
            prod_id : id
        },
        success:function(data){
            window.location.href = 'http://localhost:8000/details/${id}'
        }
    })
})


$('.minus-wishlist').click(function(){
    var id=$(this).attr('pid').toString();
    $.ajax({
        type :'GET',
        url : '/minuswishlist',
        data : {
            prod_id : id
        },
        success:function(data){
            window.location.href = 'http://localhost:8000/details/${id}'
        }
    })
})