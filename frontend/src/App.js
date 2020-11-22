import React, {useEffect} from "react";
import {Switch, Route, useHistory, useLocation} from "react-router-dom"
import HomePage from "./pages/homepage"
import "../src/styles.css"


export default function App() {

  const history = useHistory();
  const location = useLocation();

  useEffect(() => {
    if(location.pathname === '/'){
      history.push('/home');
    }
  });

  return (
    <div className="App">
      <Switch>
        <Route path="/home">
          < HomePage/>
        </Route>
      </Switch>
    </div>
  );
}
