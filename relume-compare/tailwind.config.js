/** Relume preset + Ash Riffe brand tokens */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  presets: [require("@relume_io/relume-tailwind")],
  theme: {
    extend: {
      gradientColorStops: ({ theme }) => theme("colors"),
      fontSize: {
        h1: ["3.5rem", { lineHeight: "1.1", letterSpacing: "-0.01em" }],
        h2: ["3rem", { lineHeight: "1.15", letterSpacing: "-0.01em" }],
        h3: ["2.5rem", { lineHeight: "1.2", letterSpacing: "-0.01em" }],
        h4: ["2rem", { lineHeight: "1.3", letterSpacing: "-0.01em" }],
        h5: ["1.5rem", { lineHeight: "1.4", letterSpacing: "-0.01em" }],
        h6: ["1.25rem", { lineHeight: "1.4", letterSpacing: "-0.01em" }],
        large: ["1.25rem", { lineHeight: "1.5" }],
        medium: ["1.125rem", { lineHeight: "1.5" }],
        regular: ["1rem", { lineHeight: "1.5" }],
        small: ["0.875rem", { lineHeight: "1.5" }],
        tiny: ["0.75rem", { lineHeight: "1.5" }],
      },
      colors: {
        scheme: {
          background: "#F6F1E9",
          foreground: "#FBF8F4",
          text: "#1A1614",
          border: "rgba(26,22,20,.14)",
          "btn-text": "#F6F1E9",
        },
        terracotta: "#C07B68",
        blush: "#EDD4CB",
        ink: "#1A1614",
        "ink-soft": "#6B5E58",
      },
      fontFamily: {
        serif: ['"Cormorant Garamond"', "serif"],
        sans: ["arboria", "system-ui", "sans-serif"],
      },
      borderRadius: {
        button: "0rem", card: "0rem", image: "0rem", form: "0rem",
        badge: "999px", checkbox: "0rem", carousel: "0rem", dropdown: "0rem",
      },
    },
  },
};
