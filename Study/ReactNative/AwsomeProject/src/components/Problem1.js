import React, {Component} from 'react';
import { View } from 'react-native';

export default class Problem1 extends Component{
    render() {
        return(
            <View>
                <View style={{width: 50, height:50, backgroundColor: 'blue'}}/>
                <View style={{width: 100, height: 100, backgroundColor: 'black'}} />
                <View style={{width: 150, height: 150, backgroundColor: 'red'}} />
            </View>
        );
    }
}
