import React, { useState } from 'react';
import { Modal } from '@material-ui/core';
import { ButtonStyle } from '../ProductListComponent/styles';
import { Container, ButtonUpdate, InputStyle, ModalTitle } from './styles';
import api from '../../services/api';
import { FiEdit3 } from 'react-icons/fi';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {useCount} from '../../context';

function ProductModal({id, url, img_url, brand, title, price}) {

  const [visible, setVisible] = useState(false); 
  const [newImageUrl, setNewImageUrl] = useState(url); 
  const [newUrl, setNewUrl] = useState(img_url); 
  const [newBrand, setNewBrand] = useState(brand); 
  const [newTitle, setNewTitle] = useState(title); 
  const [newPrice, setNewPrice] = useState(price); 

  const {count,setCount} = useCount();
  
  async function updateProduct(){
    try{

      const resp = await api.put(`/products/${id}`,{
        url:newUrl,
        img_url:newImageUrl,
        brand:newBrand,
        title:newTitle,
        price:Number(newPrice)
      });

      setCount(count+1);
      
      toast.success(`Updated product - ${title}!`, {
          position: "top-right",
          autoClose: 5000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
      });
      setVisible(!visible);

    }
    catch(error){
        console.log(error);
        toast.error(error.response.data.message, {
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
        <ButtonStyle onClick={() => setVisible(true) }>
            <FiEdit3 size={22} color={'green'}/>
        </ButtonStyle>
        
        <Modal
          open={visible}
          onClose={()=>{
            setVisible(!visible);
          }}
        >
          <Container>
            <ModalTitle>Update the product information</ModalTitle>
            <label><b>Product URL</b></label>
            <InputStyle defaultValue={url} onChange={(text)=>setNewPrice(text.target.value)}/>
            <label><b>Image URL</b></label>
            <InputStyle defaultValue={img_url} onChange={(text)=>setNewUrl(text.target.value)}/>
            <label><b>Brand</b></label>
            <InputStyle defaultValue={brand} onChange={(text)=>setNewBrand(text.target.value)}/>
            <label><b>Title</b></label>
            <InputStyle defaultValue={title} onChange={(text)=>setNewTitle(text.target.value)}/>
            <label><b>Price</b></label>
            <InputStyle defaultValue={price} onChange={(text)=>setNewPrice(text.target.value)}/>
            <ButtonUpdate onClick={() => updateProduct() }>
              Update
            </ButtonUpdate>
          </Container>
        
        </Modal>
      </>
  );
}

export default ProductModal;