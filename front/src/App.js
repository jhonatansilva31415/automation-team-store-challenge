import React from 'react';
import Routes from './routes';
import HeaderComponent from './components/HeaderComponent';
import {ContextProvider} from './context';

function App() {
  return (
      <ContextProvider> 
        <HeaderComponent/>
        <Routes/>
      </ContextProvider>
  );
}

export default App;