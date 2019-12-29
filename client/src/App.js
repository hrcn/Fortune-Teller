import React, { Component } from 'react';
import { BrowserRouter, Switch, Route} from 'react-router-dom';
import './App.css'

import Navbar from './components/Navbar';

import Home from './pages/Home';
import About from './pages/About';
import Face from './pages/Face';
import Hand from './pages/Hand';
import Question from './pages/Question';

class App extends Component {
  render() {
    return (
      <div>
        <BrowserRouter>
          <Navbar />
            <div className="container">
              <Switch>
                <Route exact path="/" component={Home} />
                <Route exact path="/face" component={Face} />
                <Route exact path="/hand" component={Hand} />
                <Route exact path="/question" component={Question} />
                <Route exact path="/about" component={About} />
              </Switch>
            </div>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
