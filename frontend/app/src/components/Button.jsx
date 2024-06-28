import React from 'react';

export default function Button({ onClick, caption }) {
    return (
        <button onClick={onClick}>{caption}</button>
    );
};

