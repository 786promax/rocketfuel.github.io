/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector', // Enable dark mode using the 'dark' class
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        customBlue: '#1E40AF', // Custom color example
      },
    },
  },
  plugins: [],
}
