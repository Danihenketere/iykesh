
	// ...........The codes that take care of clicking on Add To Cart....................
	
	var product_ids = document.getElementsByClassName('product-address');
	var disp = document.getElementsByClassName('disp');
	var cart_btns = document.querySelectorAll('.btn-cart');

	cart_btns.forEach((item,index)=>{
		cart_btns[index].onclick = ()=>{
		console.log('Hello');

		fetch(`add_cart/${product_ids[index].innerHTML}`)
  		.then(response => response.json())
  		.then(message =>{
  			if(message.message_error){
  				disp[index].style.visibility = 'visible';
  				disp[index].innerHTML = message.message_error;
  				disp[index].style.color = 'red';
  				disp[index].style.fontWeight = 'bold';
  				setTimeout(()=>{
  					disp[index].style.visibility = 'hidden';
  				}, 2000)
  				
  			}else if(message.message_success){
  				disp[index].style.visibility = 'visible';
  				disp[index].innerHTML = message.message_success;
  				disp[index].style.color = 'green';
  				disp[index].style.fontWeight = 'bold';
  				setTimeout(()=>{
  					disp[index].style.visibility = 'hidden';
  				}, 2000)
  				
  			}
  		});

		return false;
		}
	});
// ................The below codes takes care of the calculations in the cart...............

		const calculate = document.querySelector('.calculate');
		const subtotal = document.querySelector('.subtotal');
		const total = document.querySelector('.total');
		const tax = document.querySelector('.tax');
		const rates = document.querySelectorAll('.rate');
		const quantity = document.querySelectorAll('.quantity');
		const products = document.querySelectorAll('.product');
		const cart_id = document.querySelectorAll('.cart-id');
		const user_id = document.querySelector('.user-id');

		
		

		calculate.onclick = ()=>{
			for(var i=0; i<products.length; i++){
				products[i].innerHTML =parseInt(quantity[i].value)  * parseInt(rates[i].innerHTML) ;
				console.log(user_id.innerHTML, cart_id[i].innerHTML, quantity[i].value);
			fetch('quantum', {
   			body: JSON.stringify({ 
   				user_id: user_id,
   				cart_id: cart_id[i].innerHTML,
   				quantity: quantity[i].value
   			}),
    		method:'POST',
  			}).then(res=>res.json()).then(data=>{
  				console.log(data);
  			})

			}
			let sum = 0;
			for(var i=0; i<products.length; i++){
				sum += parseInt(products[i].innerHTML);
			
			}
			subtotal.innerHTML = sum;
			total.value = sum + parseInt(tax.innerHTML);

		}
    
// ...............The below codes take care  product page..............

var productImg =document.getElementById('product-img');
var smallImg =document.getElementsByClassName('small-img');
console.log(smallImg[0])
smallImg[0].onclick = ()=>{
	productImg.src = smallImg[0].src;
}
smallImg[1].onclick = ()=>{
	productImg.src = smallImg[1].src;
}
smallImg[2].onclick = ()=>{
	productImg.src = smallImg[2].src;
}
smallImg[3].onclick = ()=>{
	productImg.src = smallImg[3].src;
}



// var makePayment = document.querySelector('#make-payment');
// makePayment.onclick = ()=>{
// 	console.log('Hello World')
// 	window.open('payment/index.html');
// }