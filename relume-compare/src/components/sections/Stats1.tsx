import { Button, type ButtonProps } from "@/components/ui/button";

type StatsProps = { percentage: string; heading: string };

type Props = {
  tagline: string;
  heading: string;
  description: string;
  buttons: ButtonProps[];
  stats: StatsProps[];
};

export type Stats1Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Stats1 = (props: Stats1Props) => {
  const { tagline, heading, description, stats, buttons } = {
    ...Stats1Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <div className="mb-12 grid grid-cols-1 gap-y-5 md:mb-18 md:grid-cols-2 md:gap-x-12 lg:mb-20 lg:gap-x-[5.25rem]">
          <div>
            <p className="mb-3 font-semibold md:mb-4 text-terracotta uppercase tracking-[.2em] text-tiny">{tagline}</p>
            <h2 className="text-h2 font-bold">{heading}</h2>
          </div>
          <div>
            <p className="text-medium text-ink-soft">{description}</p>
            <div className="mt-6 flex flex-wrap items-center gap-4 md:mt-8">
              {buttons.map((button, index) => (
                <Button key={index} {...button}>
                  {button.title}
                </Button>
              ))}
            </div>
          </div>
        </div>
        <div className="grid grid-cols-1 gap-y-8 md:grid-cols-3 md:gap-x-8 lg:gap-x-12 lg:gap-y-16">
          {stats.map((stat, index) => (
            <div key={index} className="border-l border-scheme-border pl-8">
              <p className="mb-2 text-[3.5rem] leading-[1.3] font-bold md:text-[4rem] lg:text-[5rem] font-serif">
                {stat.percentage}
              </p>
              <h3 className="text-h6 font-bold">{stat.heading}</h3>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export const Stats1Defaults: Props = {
  tagline: "",
  heading: "",
  description: "",
  buttons: [],
  stats: [],
};
