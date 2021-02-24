import styled from 'styled-components';
import {firstMediaQuery,secondMediaQuery,thirdMediaQuery} from '../../helpers/utils'

export const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 50px;

    @media screen and (max-width:${thirdMediaQuery}px){
        padding:20px;
        text-align:center;
    }
`

export const Title = styled.h1`
    font-size: 45px;
    
`

export const Paragraph = styled.p`
    font-size: 15px;
    
    @media screen and (max-width:${secondMediaQuery}px){
        padding:15px;
        text-align:center;
    }
`
