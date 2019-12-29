import React, { Component } from 'react';

import Grid from '@material-ui/core/Grid';

class About extends Component {
    render() {
        return (
            <Grid container>
                <Grid item xs/>
                <Grid item xs>
                    <p>Since ancient times, people believe in multiple ways of divinations, includes constellation, Chinese Zodiac, palmistry and physiognomy, etc.</p>
                    <p>Traditionally, people tend to visit different augurs face to face for practise divination, and the augur predicts those people fortune based on experience or specific rules.</p>
                    <p>This project is going to provide a new and reliable way for people who believe in divination and desire for quickly accessing to any kinds of divinations or combined fortune.</p>
                    <p>It aims to integrate most of traditional ways of divination by building a database, which stores all specific rules of divination, and also a pattern recognizing model to replace augur’s visual method.</p>
                    <p>By integrating, digitalizing, and formulating these information, a precise way of divination without human error will surely change the way people’s way of divination or even belief.</p>
                </Grid>
                <Grid item xs/>
            </Grid>
        )
    }
}

export default About;
