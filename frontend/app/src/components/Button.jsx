import React from 'react';

export default function Button({ onClick, caption = "", className }) {
    return (
        <button onClick={onClick} className={className}>{caption}</button>
    );
};


