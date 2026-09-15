import React, { useState } from 'react';

export default function App() {
  const [cartCount, setCartCount] = useState(0);

  return (
    <div style={{ backgroundColor: '#070708', color: '#fff', minHeight: '100vh', padding: '20px', fontFamily: 'sans-serif' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #D4AF37', paddingBottom: '15px' }}>
        <h1 style={{ color: '#D4AF37', fontSize: '28px', letterSpacing: '2px', margin: 0 }}>AURA GOLD</h1>
        <div>Cart: <span style={{ color: '#D4AF37', fontWeight: 'bold' }}>{cartCount}</span></div>
      </header>

      <main style={{ textAlign: 'center', marginTop: '60px' }}>
        <h2 style={{ fontSize: '36px', color: '#D4AF37' }}>Timeless Luxury & Craftsmanship</h2>
        <p style={{ color: '#aaa', maxWidth: '600px', margin: '20px auto' }}>
          Discover our handcrafted collection of premium watches, necklaces, rings, and bracelets.
        </p>
        <button 
          onClick={() => setCartCount(cartCount + 1)}
          style={{ backgroundColor: '#D4AF37', color: '#000', border: 'none', padding: '12px 24px', fontWeight: 'bold', cursor: 'pointer', borderRadius: '4px', marginTop: '20px' }}
        >
          Add Featured Watch to Cart
        </button>
      </main>
    </div>
  );
}
