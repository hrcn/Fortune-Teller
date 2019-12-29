import React, { Component } from 'react';
import withStyles from '@material-ui/core/styles/withStyles';
import PropTypes from 'prop-types';
import axios from 'axios';

// Material UI
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import MenuItem from '@material-ui/core/MenuItem';

// styling settings
const styles = {
    form: {
        textAlign: 'center',
        color: ''
    },
    pageTitle: {
        margin: 'auto',
    },
    textField: {
        margin: 'auto',
        marginTop: '15px',
        width: 300
    },
    button: {
        marginTop: '20px',
        width: 300
    },
    input: {
        marginTop: '20px',
    }
}

// array of genders
const genders = [
    { value: 'Male', label: 'Male'},
    { value: 'Female', label: 'Female'}
]

// array of constellations
const constellations = [
    { value: 'Aries', label: 'Aries'},
    { value: 'Taurus', label: 'Taurus'},
    { value: 'Gemini', label: 'Gemini'},
    { value: 'Cancer', label: 'Cancer'},
    { value: 'Leo', label: 'Leo'},
    { value: 'Virgo', label: 'Virgo'},
    { value: 'Libra', label: 'Libra'},
    { value: 'Scorpio', label: 'Scorpio'},
    { value: 'Sagittarius', label: 'Sagittarius'},
    { value: 'Capricorn', label: 'Capricorn'},
    { value: 'Aquarius', label: 'Aquarius'},
    { value: 'Pisces', label: 'Pisces'}
]

class Form extends Component {
    constructor() {
        super();
        this.state = {
            name: '',
            gender: '',
            phone: '',
            birthday: '',
            constellation: '',
            // handimageID: null,
            // faceimageID: null
        }
    }

    handleSubmit = (event) => {
        alert('Form Submitted!');

        event.preventDefault();
        console.log(this.state);

        axios.post('http://localhost:4000/api/newuser', this.state)
        .then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })
        
    }

    handleChange = (event) => {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    render() {

        const { classes } = this.props;

        return (
            <Grid container className={classes.form}>
                <Grid item sm/>
                <Grid item sm>
                    <Typography variant="h5" className={classes.pageTitle}>
                        Let's begin with some basic info!
                    </Typography>
                    <form noValidate className={classes.container} onSubmit={this.handleSubmit} autoComplete="off">
                        <TextField
                            required
                            name="name"
                            label="Full Name"
                            className={classes.textField}
                            value={this.state.name}
                            onChange={this.handleChange}
                            fullWidth
                            margin="normal"
                        />
                        
                        <TextField
                            required
                            select
                            name="gender"
                            label="Select Your Gender"
                            className={classes.textField}
                            value={this.state.gender}
                            onChange={this.handleChange}
                            SelectProps={{
                                MenuProps: {
                                className: classes.menu,
                                },
                            }}
                            margin="normal"
                            >
                            {genders.map(option => (
                                <MenuItem key={option.value} value={option.value}>
                                {option.label}
                                </MenuItem>
                            ))}
                        </TextField>

                        <TextField
                            required
                            name="phone"
                            label="Phone Number"
                            className={classes.textField}
                            value={this.state.phone}
                            onChange={this.handleChange}
                            fullWidth
                            margin="normal"
                        />

                        <TextField
                            required
                            name='birthday'
                            label="Birthday"
                            type="date"
                            className={classes.textField}
                            value={this.state.birthday}
                            onChange={this.handleChange}
                            // in order not to block the input field
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />

                        <TextField
                            required
                            select
                            name="constellation"
                            label="Select Your Constellation"
                            className={classes.textField}
                            value={this.state.constellation}
                            onChange={this.handleChange}
                            SelectProps={{
                                MenuProps: {
                                className: classes.menu,
                                },
                            }}
                            margin="normal"
                            >
                            {constellations.map(option => (
                                <MenuItem key={option.value} value={option.value}>
                                {option.label}
                                </MenuItem>
                            ))}
                        </TextField>
                        
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
    }
}

Form.propTypes = {
    classes: PropTypes.object.isRequired
}

export default withStyles(styles)(Form);