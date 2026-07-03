import React from "react";

type ListItem = {
  num: string;
  heading: string;
  description: string;
};

type Props = {
  tagline: string;
  heading: string;
  description: string;
  listItems: ListItem[];
};

export type Layout629Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

// Vendored fixes vs Relume source: (1) props were spread BEFORE defaults,
// so custom content never applied; (2) it rendered listItems[0]/[1] twice
// instead of all four. Icons swapped for numbered marks per brand.
export const Layout629 = (props: Layout629Props) => {
  const { tagline, heading, description, listItems } = {
    ...Layout629Defaults,
    ...props,
  };

  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className="mb-12 grid grid-cols-1 gap-x-8 gap-y-5 md:mb-18 md:grid-cols-2 md:gap-x-12 lg:mb-20 lg:gap-x-20">
          <div>
            <p className="mb-3 font-semibold md:mb-4 text-terracotta uppercase tracking-[.2em] text-tiny">{tagline}</p>
            <h2 className="text-h2 font-bold">{heading}</h2>
          </div>
          <div className="md:mt-0">
            <p className="text-medium text-ink-soft">{description}</p>
          </div>
        </div>

        {/* Renders EVERY item (the stock component hard-rendered 4 slots,
            which lied under a "Seven pillars" heading) */}
        <div className="grid grid-cols-1 gap-x-12 border-t border-scheme-border md:grid-cols-2">
          {listItems.map((item, i) => (
            <Item key={i} item={item} />
          ))}
        </div>
      </div>
    </section>
  );
};

const Item = ({ item }: { item: ListItem }) => {
  if (!item) return <div />;
  return (
    <div className="border-b border-scheme-border py-6 md:py-8">
      <div className="grid grid-cols-[auto_1fr] items-baseline gap-6">
        <p className="font-serif italic text-h6 text-terracotta">{item.num}</p>
        <div>
          <h3 className="mb-2 text-h5 font-bold">{item.heading}</h3>
          <p className="text-ink-soft">{item.description}</p>
        </div>
      </div>
    </div>
  );
};

export const Layout629Defaults: Props = {
  tagline: "",
  heading: "",
  description: "",
  listItems: [],
};
