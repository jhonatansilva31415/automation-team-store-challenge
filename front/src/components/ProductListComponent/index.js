import React, { useEffect, useState } from 'react';
import api from '../../services/api';
import ProductModal from '../ProductModal';
import { Container, 
         ContainerItem, 
         ContainerText, 
         ContainerButtons, 
         ButtonStyle,
         ProductSearch
        } from './styles';
import {FiTrash, FiEdit3} from 'react-icons/fi';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {useCount} from '../../context';

function ProductList() {

    const [products, setProduct] = useState([]);
    const [visible, setVisible] = useState(false); 
    const [searchTerm, setSearchTerm] = useState('');
    
    const {count} = useCount();

    useEffect(()=>{
        const load = async () => {
            const resp = await api.get('/products');
            setProduct(resp.data);
        }
        load()
    }, [count]);

    async function deleteProductByID(product_id, title){
        try{
            await api.delete(`/products/${product_id}`);
            setProduct(products.filter(
                (product) => product.id !== product_id
            ));
            toast.success(`Deleted product - ${title}!`, {
                position: "top-right",
                autoClose: 5000,
                hideProgressBar: false,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
            });
        }
        catch(error){
            console.log(error);
            toast.error('Error!', {
                position: "top-right",
                autoClose: 5000,
                hideProgressBar: false,
                closeOnClick: true,
                pauseOnHover: true,
                draggable: true,
                progress: undefined,
            });
        }
    }

    return (
        <>
            <ContainerItem>
                <ProductSearch placeholder="Search" onChange={(event)=>setSearchTerm(event.target.value)} />
            </ContainerItem>
            <Container>
                
                {   
                    products.filter((product)=>{
                        if (searchTerm == ''){
                            return product
                        }
                        else{
                            let searchTitle = product.title.toLowerCase().includes(searchTerm.toLowerCase())
                            let searchBrand = product.brand.toLowerCase().includes(searchTerm.toLowerCase())
                            if (searchTitle || searchBrand) return product;
                        }
                    }).map((product)=>(
                        <ContainerItem key={product.id}>  
                            <img src={product.img_url} style={{width:300,height:300}}/>
                            <ContainerButtons>
                                <ProductModal 
                                    id={product.id}
                                    url={product.url}
                                    img_url={product.img_url}
                                    brand={product.brand}
                                    title={product.title}
                                    price={product.price}
                                /> 
                                <ButtonStyle onClick={() => deleteProductByID(product.id, product.title)}>
                                    <FiTrash size={22} color={'red'}/>
                                </ButtonStyle>
                            </ContainerButtons>
                            <ContainerText>  
                                <b>{product.brand}</b>
                                <h4>{product.title}</h4>
                                {product.price.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                            </ContainerText>
                        </ContainerItem>
                    ))
                }
                <ToastContainer
                    position="top-right"
                    autoClose={5000}
                    hideProgressBar={false}
                    newestOnTop={false}
                    closeOnClick
                    rtl={false}
                    pauseOnFocusLoss
                    draggable
                    pauseOnHover
                    />
                <ToastContainer />
            </Container>
        </>
    )
}

export default ProductList;