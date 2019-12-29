import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';

class Navbar extends Component {
    render() {
        return (
            <AppBar>
                <Toolbar className="nav-container">
                    <Button color="inherit" component={Link} to="/">
                        Home
                    </Button>
                    <Button color="inherit" component={Link} to="/face">
                        Face
                    </Button>
                    <Button color="inherit" component={Link} to="/hand">
                        Hand
                    </Button>
                    <Button color="inherit" component={Link} to="/question">
                        Question
                    </Button>
                    <Button color="inherit" component={Link} to="/about">
                        About
                    </Button>
                </Toolbar>
            </AppBar>
        )
    }
}

export default Navbar;
