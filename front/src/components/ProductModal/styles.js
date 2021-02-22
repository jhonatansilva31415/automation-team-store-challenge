import styled from 'styled-components';
import {firstMediaQuery,secondMediaQuery,thirdMediaQuery,forthMediaQuery} from '../../helpers/utils'

export const Container = styled.div`
    background-color: white;
    margin:200px;
    margin-left: 600px !important; 
    margin-right: 600px !important;
    height: 600px;
    border:0;
    outline: none;
    border-radius: 7px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    @media screen and (max-width:${firstMediaQuery}px){
        height: 600px;
        margin: 200px;
        margin-left: 300px !important; 
        margin-right: 300px !important;
    }
    @media screen and (max-width:${secondMediaQuery}px){
        height: 600px;
        margin: 200px;
        margin-left: 100px !important; 
        margin-right: 100px !important;
    }

    @media screen and (max-width:${thirdMediaQuery}px){
        height: 600px;
        margin: 200px;
        margin-left: 50px !important; 
        margin-right: 50px !important;
    }

    @media screen and (max-width:${forthMediaQuery}px){
        height: 400px;
        margin: 100px;
        margin-left: 15px !important; 
        margin-right: 15px !important;
    }

`

export const ButtonUpdate =  styled.button`
    font-size: 15px;
    padding: 15px;
    margin-top: 25px;
    border-radius: 4px;
    border: 0;
    background-color: #4CAF50;
    outline:none;
    transition-duration: 0.5s;
    color:white;
    &:hover{
        background: #006600;
        border-radius: 8px;
    }

`


export const InputStyle =  styled.input`
    font-size: 15px;
    padding: 10px;
    margin-bottom: 10px;
    border-top:0;
    border-right:0;
    border-left:0;
    width:85%;
    outline:none;
    transition-duration: 0.5s;
    &:hover{
        background-color:#989898;	
        color:white;
    }
    &:focus{
        border-bottom-color: lightgreen;
    }

    @media screen and (max-width:${forthMediaQuery}px){
        font-size: 10px;
        padding: 5px;
        margin-bottom: 5px;
        border-top:0;
        border-right:0;
        border-left:0;
        width:85%;
    }
`

export const ModalTitle = styled.h2`
    font-size:20px;
    margin: 0 0 30px 0;
    font-weight: bold;

    @media screen and (max-width:${forthMediaQuery}px){
        font-size:18px;
        margin: 0 0 5px 0;
        font-weight: bold;
    }
` 

