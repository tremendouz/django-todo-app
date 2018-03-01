import React, { Component } from 'react';
import { render } from 'react-dom';

import '../styles/style.css';

import logoImage from '../assets/logo.svg';

export default class Hello extends Component {
    render() {
        return (
            <div>
                Hello from react
                <img src={logoImage} alt="logo" />
            </div>
        );
    }
}

render(<Hello />, document.getElementById('app'));