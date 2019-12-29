import React, { Component } from 'react';
import withStyles from '@material-ui/core/styles/withStyles';
import PropTypes from 'prop-types';
import axios from 'axios';

// Material UI
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { DropzoneArea } from 'material-ui-dropzone'

const styles = {
    form: {
        textAlign: 'center',
        color: ''
    },
    pageTitle: {
        margin: 'auto',
    },
    selectField: {
        marginTop: '20px',
        width: 300
    },
    dropZone: {
        marginTop: '20px',
        width: 450
    }
}

class HandForm extends Component {
    constructor() {
        super();
        this.state = {
            handImage: [],
            isLoaded: false
        }
    }

    handleSubmit = (event) => {
        event.preventDefault();
        console.log(this.state);

        const fd = new FormData();
        fd.append('handImage', this.state.handImage);

        const config = {
            headers: { "content-type": "multipart/form-data", 'Access-Control-Allow-Origin': '*'}
        }

        // post data to express
        axios.post('http://localhost:4000/api/newhand', fd, config)
        .then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })

        // post data to flask
        axios.post('http://localhost:5000/api/newhand', fd, config)
        .then(response => {
            console.log(response)
            this.setState({handImage: response.data, isLoaded: true})
            console.log(this.state)
        })
        .catch(error => {
            console.log(error)
        })
        
    }

    handleImageUpload = (files) => {
        this.setState({
            handImage: files[0]
        });
        console.log(files[0]);
    }

    render() {

        const { classes } = this.props;
        const { isLoaded } = this.state;

        if(!isLoaded) {
            return (
                <Grid container className={classes.form}>
                    <Grid item sm/>
                    <Grid item sm>
                        <Typography variant="h5" className={classes.pageTitle}>
                            Palm Prediction
                        </Typography>
                        <form noValidate className={classes.container} onSubmit={this.handleSubmit} autoComplete="off">
                            <DropzoneArea
                                dropzoneClass={classes.dropZone}
                                onChange={this.handleImageUpload}
                                dropzoneText='Upload Palm Image (.jpg Format) Here'
                                acceptedFiles={['image/jpeg']}
                                filesLimit={1}
                            />
    
                            <p>* The image should be clear.</p>
    
                            <Button
                                type="submit" 
                                variant="contained" 
                                color="primary"
                                className={classes.button}
                                fullWidth>
                                    SUBMIT
                            </Button>
                        </form>
                    </Grid>
                    <Grid item sm/>
                </Grid>
            );
        } else {
            return (
                <Grid container className={classes.form}>
                    <Grid item sm/>
                    <Grid item sm>
                        <img src={`data:image/png;base64,${this.state.handImage}`} alt=""/>
                    </Grid>
                    <Grid item sm/>
                </Grid>
            )
        }
    }
}

HandForm.propTypes = {
    classes: PropTypes.object.isRequired
}

export default withStyles(styles)(HandForm);