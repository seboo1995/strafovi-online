let select = document.getElementById('select-size')
select.addEventListener('change', function (){

    let p_div = document.getElementById('prod-info');
    let ul_list = document.createElement('ul')
    ul_list.classList.add('list-bullets')
    const tip = document.getElementsByTagName('h1')[1].innerHTML;
    if (tip.includes('Штраф')){
    const value_selected = select.value;
    p_div.innerHTML = ''
    let selected_option
    console.log('VALUE SELECTED:',value_selected)
    for (const option of select.childNodes) {
        if(value_selected === option.value){
            selected_option = option
            break
        }

    }
    let data_obj = make_prod_json(selected_option.dataset.item)

    let debelina_value = remove_trailing_zeros_from_float(data_obj.Debelina.replace(/['"]+/g, ''))
    let dolzina_value = remove_trailing_zeros_from_float(data_obj.Dolzina.replace(/['"]+/g, ''))
    let cena_value = remove_trailing_zeros_from_float(data_obj.Cena.replace(/['"]+/g, ''))
    let glava_value = data_obj.Glava
    let title = data_obj.Ime.replace(/['"]+/g, '')



    // make h4 tag poveke informacii
    let pov_info = document.createElement('h4')
    pov_info.classList.add('mb-4')
    pov_info.innerHTML = 'Poveke informacii za proizvodot'
    p_div.appendChild(pov_info)

    // make ul list

    //make li
    //name
    let ime = create_li_and_class('Име на производ', title)
    // debelina
    ul_list.appendChild(ime)
    let debelina = create_li_and_class('Дебелина',debelina_value)
    //dolzina
    ul_list.appendChild(debelina)
    let dolzina = create_li_and_class('Должина',dolzina_value)
    ul_list.appendChild(dolzina)
    //glava
    let glava = create_li_and_class('Глава',glava_value)
    ul_list.appendChild(glava)
    //cena
    let cena = create_li_and_class('Цена',cena_value)
    ul_list.appendChild(cena)
    }

    else{
    let ul_list = document.createElement('ul')
    ul_list.classList.add('list-bullets')

    }



    p_div.appendChild(ul_list)
    let add_to_cart_html  = ` <div class="center" id='add_to_cart'>
    <div class="buttons d-flex flex-row">
        <button class="btn btn-success cart-button px-5"><span class="dot"></span>Add to cart </button>
    </div>
</div>
</div>`
p_div.innerHTML +=add_to_cart_html



});


function create_li_and_class(item_prop, item_val) {
    let item = document.createElement('li')
    item.innerHTML = "<b>"+item_prop+"</b>"+ ":" + item_val + ""
    return item
}



function make_prod_json(s){
    let empty_dict  = {}
    let json_to_arr = s.replace('{','').replace('}','').split(',')
    for (const item of json_to_arr) {
        let key_value = item.split(':')
        let key = key_value[0].replace(/[']+/g, '').replace(/["]+/g, '').trim()
        let value = key_value[1].trim()
        empty_dict[key]=value
        
    }
    return empty_dict


}
function remove_trailing_zeros_from_float(num){
// num is actually a string
return num.replace('.0','')

}


