import { Header138 } from "@/components/sections/Header138";
import { Stats1 } from "@/components/sections/Stats1";
import { Portfolio15 } from "@/components/sections/Portfolio15";
import { Testimonial1 } from "@/components/sections/Testimonial1";
import { Layout629 } from "@/components/sections/Layout629";
import { Content2 } from "@/components/sections/Content2";
import { Cta1 } from "@/components/sections/Cta1";

const nav = (
  <nav className="fixed top-0 left-0 right-0 z-50 border-b border-scheme-border bg-scheme-background/90 backdrop-blur">
    <div className="container flex items-center justify-between px-[5%] py-4">
      <a href="#" className="font-serif text-xl font-semibold tracking-[.2em]">ASH RIFFE</a>
      <div className="flex items-center gap-8 text-small">
        <a href="#">Work</a><a href="#">Ethos</a><a href="#">About</a><a href="#">Contact</a>
      </div>
    </div>
  </nav>
);

export default function App() {
  return (
    <div className="font-sans">
      {nav}
      <Header138
        heading={
          <>
            <span className="italic text-terracotta font-medium">A lasting conversation</span>
            <br />
            <span className="uppercase tracking-wide">between past &amp; future.</span>
          </>
        }
        description="Interior architecture for homes and spaces in Seattle. Considered, livable, and made to last. Built around how you actually live."
        buttons={[{ title: "View the work", variant: "secondary" }]}
        firstImage={{ src: "/img/hero-living.webp", alt: "Open-plan living room with warm wood ceiling" }}
        secondImage={{ src: "/img/theater.webp", alt: "Ridges Theater moodboard detail" }}
      />
      <Stats1
        tagline="Seattle, WA"
        heading="Interior architecture, grounded in real experience."
        description="Nearly a decade in Seattle's luxury furniture world taught Ash how materials, makers, and clients actually work together."
        buttons={[]}
        stats={[
          { percentage: "10", heading: "Years in luxury showrooms" },
          { percentage: "7", heading: "Pillars of design philosophy" },
          { percentage: "2026", heading: "BFA, Interior Architecture" },
        ]}
      />
      <Portfolio15
        tagline="Portfolio"
        heading="Selected work."
        description="Residential and commercial projects, from first sketch to finished room."
        projects={[
          {
            title: "The Healing Womb",
            description: "Long-term housing for domestic violence survivors, designed around restoration and autonomy.",
            image: { src: "/img/healing-womb.webp", alt: "The Healing Womb design board" },
            url: "#", button: { title: "View project", variant: "link", size: "link" },
            tags: [{ label: "Housing Design", url: "#" }, { label: "Concept", url: "#" }],
          },
          {
            title: "Alden Fine Arts Library",
            description: "A university fine-art library modernization: living plant walls, rotating student art, daylight pulled deep into the stacks.",
            image: { src: "/img/library.webp", alt: "Alden Fine Arts Library board" },
            url: "#", button: { title: "View project", variant: "link", size: "link" },
            tags: [{ label: "Academic", url: "#" }, { label: "Concept", url: "#" }],
          },
          {
            title: "The Ridges Theater",
            description: "A palette that holds up under stage light and house light alike: terra cotta, mauve brick, and brushed copper.",
            image: { src: "/img/theater.webp", alt: "Ridges Theater moodboard" },
            url: "#", button: { title: "View project", variant: "link", size: "link" },
            tags: [{ label: "Performing Arts", url: "#" }, { label: "Concept", url: "#" }],
          },
          {
            title: "Bright Start Daycare",
            description: "A commercial childcare interior that takes color seriously without shouting.",
            image: { src: "/img/daycare.webp", alt: "Bright Start Daycare render" },
            url: "#", button: { title: "View project", variant: "link", size: "link" },
            tags: [{ label: "Commercial", url: "#" }, { label: "Concept", url: "#" }],
          },
        ]}
        button={{ title: "See all seven", variant: "secondary" }}
      />
      <Testimonial1
        quote={'"Design as a lasting conversation between past, present, and future: honoring history, respecting the environment, and elevating daily living."'}
        avatar={{ src: "/img/portrait.webp", alt: "Ash Riffe" }}
        name="Ash Riffe"
        position="Design Ethos"
      />
      <Layout629
        tagline="Philosophy"
        heading="Seven pillars."
        description="Every project rests on the same foundations: the principles that decide what stays, what goes, and why."
        listItems={[
          { num: "01", heading: "Timeless Elegance", description: "Enduring quality, subtle luxury, proportion and restraint." },
          { num: "02", heading: "Biophilic Design", description: "Nature, daylight, organic forms, and indoor-outdoor harmony." },
          { num: "03", heading: "Sustainability & Longevity", description: "Material honesty, durable essentials, adaptive reuse." },
          { num: "04", heading: "Bold Colors & Artistic Flair", description: "Color as narrative, artistic collaboration, playful restraint." },
        ]}
      />
      <Content2
        heading="Trained to see what most people miss."
        image={{ src: "/img/portrait.webp", alt: "Ash Riffe in Paris" }}
      >
        <div>
          <p>
            Ash Riffe is a Seattle-based interior architecture designer, graduating with her BFA
            from Ohio University in 2026. Her first memory of architecture is Frank Lloyd Wright's
            Lowell and Agnes Walter House in small-town Iowa, at age seven. The pull never let go.
          </p>
          <p>
            Nearly a decade in Seattle's luxury furniture world (B&amp;B Italia, Inform Interiors,
            Codor Design, J. Garner Home, Alchemy Collections) taught her how materials, makers,
            and clients actually work together. Her spaces are classic with an edge: clean lines,
            honest materials, collected and layered.
          </p>
        </div>
      </Content2>
      <Cta1
        heading="Ready to start the conversation?"
        description="Book a free 5-minute consultation. No cost, no pressure."
        buttons={[{ title: "Book a Free Consultation" }]}
        image={{ src: "/img/carmel.jpg", alt: "Carmel by the Sea living room" }}
      />
    </div>
  );
}
