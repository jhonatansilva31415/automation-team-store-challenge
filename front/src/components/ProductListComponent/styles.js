import styled from 'styled-components';
import {firstMediaQuery,secondMediaQuery,thirdMediaQuery} from '../../helpers/utils'


export const Container = styled.div`
    display:grid;
    grid-template-columns: 1fr 1fr 1fr;
    justify-content: center;
    align-items: center;
    margin:0 auto;
    width: 60%;
    height: 100vh;
    

    @media screen and (max-width:${firstMediaQuery}px){
        grid-template-columns: 1fr 1fr;
        width: 80%;
    }

    @media screen and (max-width:${secondMediaQuery}px){
        grid-template-columns: 1fr;
    }

    @media screen and (max-width:${thirdMediaQuery}px){
        grid-template-columns: 1fr;
    }
`


export const ContainerItem = styled.div`
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top:40px;
`

export const ContainerText = styled.div`
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    margin-top:15px;
`

export const ContainerButtons =  styled.div`
    display:flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    width: 100px;
    margin-top:15px;
`

export const ButtonStyle =  styled.button`
    border: 0;
    background: none;
    outline:none;
    transition-duration: 0.5s;
    &:hover{
        background: #E8E8E8;
        border-radius: 5px;
    }
`

export const ProductSearch =  styled.input`
    font-size: 15px;
    padding: 10px;
    margin-bottom: 10px;
    border-top:0;
    border-right:0;
    border-left:0;
    width:35%;
    outline:none;
    transition-duration: 0.5s;

    &:hover{
        background-color:#F8F8F8;	
    }
    &:focus{
        border-bottom-color: green;
    }


    @media screen and (max-width:${firstMediaQuery}px){
        width:40%;
    }
    @media screen and (max-width:${secondMediaQuery}px){
        width:60%;
    }
    @media screen and (max-width:${thirdMediaQuery}px){
        width:70%;
    }
`

