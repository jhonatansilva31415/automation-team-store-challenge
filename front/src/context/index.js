import React, {useContext,useState,createContext} from 'react';

const context = createContext()

function ContextProvider({children}) {
  
    const [count,setCount] = useState(0);
    
    return (
        <context.Provider
            value={{count,setCount}}
        >
            {children}
        </context.Provider>
    );
}

function useCount(){
    const contextCount = useContext(context);
    return contextCount;
}


export {ContextProvider,useCount};