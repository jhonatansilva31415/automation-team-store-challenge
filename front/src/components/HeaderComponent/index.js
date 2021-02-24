import React from 'react';

import { Container, Title, Paragraph } from './styles';

function HeaderComponent() {
  return (
            <Container>
                <Title>Automation Challenge</Title>
                <Paragraph>
                  This a project for the automation challenge, you can edit and delete 
                  products that were uploaded to the API 
                </Paragraph>
            </Container>
  )
            
}

export default HeaderComponent;