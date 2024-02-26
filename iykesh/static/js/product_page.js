
	
  // ...........The codes that take care of clicking on Add To Cart....................
	
	var product_ids = document.getElementsByClassName('product-address');
	var disp = document.querySelectorAll('.disp');
	var cart_btns = document.querySelectorAll('.btn-cart');

	cart_btns.forEach((item,index)=>{
		cart_btns[index].onclick = ()=>{
		console.log('Hello');

		fetch(`add_cart/${product_ids[index].innerHTML}`)
  		.then(response => response.json())
  		.then(message =>{
        console.log('Hello');
  			if(message.message_error){
  				disp[index].style.visibility = 'visible';
  				disp[index].innerHTML = message.message_error;
  				disp[index].style.color = 'red';
  				disp[index].style.fontWeight = 'bold';
  				setTimeout(()=>{
  					disp[index].style.visibility = 'hidden';
  				}, 2000);
  				
  			}else if(message.message_success){
  				disp[index].style.visibility = 'visible';
  				disp[index].innerHTML = message.message_success;
  				disp[index].style.color = 'green';
  				disp[index].style.fontWeight = 'bold';
  				setTimeout(()=>{
  					disp[index].style.visibility = 'hidden';
  				}, 2000);
  				
  			}
  		});

		return false;
		}
	});

// ...............The below codes take care  product page..............

var productImg =document.getElementById('product-img');
var smallImg =document.getElementsByClassName('small-img');
// console.log(smallImg[0])
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


// The script that  taked care of related products

const tableOutput = document.querySelector('.table-output');
const prdctid = document.querySelector('.prdctid').innerHTML;

fetch('related_products', {
    body: JSON.stringify({ searchText: prdctid}),
    method:'POST',
  }).then(res=>res.json()).then(data=>{

    console.log('data', data);

    if(data.length === 0){
      tableOutput.innerHTML = 'No related product found';

    }else{
      tableOutput.innerHTML = '';
      data.forEach(item=>{
        tableOutput.innerHTML += `
        <div class="product-items">
              <div class="product">
                <i class="disp"></i>
                <br>
                <br>
                <div class="product-content">
                  <div class="product-img">
                    <a href="${item.id}"><img src="media/${item.original_pics}" width="200" height="200" alt="product image"></a>
                  </div>
                </div>
                <br>
                <div product-info>
                  <div class="product-info-top">
                    <h4 class="sm-title">lifestyle</h4>
                    <div class="rating">
                      <span><i class="fa fa-star"></i></span>
                      <span><i class="fa fa-star"></i></span>
                      <span><i class="fa fa-star"></i></span>
                      <span><i class="fa fa-star"></i></span>
                      <span><i class="fa fa-star"></i></span>
                    </div>
                  </div>
                  <a href="" class="product-name">${item.name}&nbsp;&nbsp;SE<span class="product-address">${item.id}</span>AB</a>
                  <div class="product-price" style="display: flex; padding-bottom: 0;">
                  <p >N ${item.initial_price}</p>
                  <p >N ${item.final_price}</p>
                  </div>
                </div>
                <!-- <div class="off-info">
                  <h2 class="sm-title">25% off</h2>
                </div> -->
              </div>

            </div>`;
      });
      
    }
  });



// ....This will handle the only product page add to cart button.....


  var productid = document.querySelector('.prdctid');
  var span = document.querySelector('.span1');
  var cartbtn = document.querySelector('.btn-cart1');

 console.log(productid);
    cartbtn.onclick = ()=>{
    // console.log('Hello');

    fetch(`products/add_cart/${productid.innerHTML}`)
      .then(response => response.json())
      .then(message =>{
        // console.log('Hello');
        if(message.message_error){
          span.style.visibility = 'visible';
          span.innerHTML = message.message_error;
          span.style.color = 'red';
          span.style.fontWeight = 'bold';
          setTimeout(()=>{
            span.style.visibility = 'hidden';
          }, 2000);
          
        }else if(message.message_success){
          span.style.visibility = 'visible';
          span.innerHTML = message.message_success;
          span.style.color = 'green';
          span.style.fontWeight = 'bold';
          setTimeout(()=>{
            span.style.visibility = 'hidden';
          }, 2000);
          
        }
      });

    return false;
    }
  