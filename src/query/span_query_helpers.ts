// This file is intentionally hand-authored instead of generated. It derives
// ergonomic enum codecs and public query names from the generated protobuf
// enums while living outside generated output so it survives schema regen.
import {
  AggregateGroupField,
  AggregateMetric,
  CastType,
  DecodeStrategy,
  SelectableSpanField,
  SortDirection,
  SpanSortField,
  TimeBucket,
} from "../../generated/ts/query/span_query";

type EnumLike = Record<string, string | number>;

type EnumForwardKey<E extends EnumLike> = Exclude<
  {
    [K in Extract<keyof E, string>]: E[K] extends number ? K : never;
  }[Extract<keyof E, string>],
  "UNSPECIFIED"
>;

type EnumValue<E extends EnumLike> = E[EnumForwardKey<E>] & number;

type SnakeToCamelCase<S extends string> = S extends `${infer Head}_${infer Tail}`
  ? `${Lowercase<Head>}${Capitalize<SnakeToCamelCase<Tail>>}`
  : Lowercase<S>;

export interface EnumCodec<TName extends string, TValue extends number> {
  readonly names: readonly TName[];
  readonly values: readonly TValue[];
  readonly byName: Readonly<Record<TName, TValue>>;
  readonly byValue: Readonly<Record<TValue, TName>>;
  normalize(value: string | number): TName | null;
  isName(value: unknown): value is TName;
  isValue(value: unknown): value is TValue;
}

function hasOwn(value: object, key: PropertyKey): boolean {
  return Object.prototype.hasOwnProperty.call(value, key);
}

function snakeToCamelCase(value: string): string {
  return value.toLowerCase().replace(/_([a-z0-9])/g, (_, char: string) => char.toUpperCase());
}

function createEnumCodec<E extends EnumLike, TName extends string>(
  enumObject: E,
  mapKey: (key: EnumForwardKey<E>) => TName,
): EnumCodec<TName, EnumValue<E>> {
  const entries = Object.entries(enumObject).filter(
    (entry): entry is [EnumForwardKey<E>, EnumValue<E>] =>
      entry[0] !== "UNSPECIFIED" && typeof entry[1] === "number",
  );

  const pairs = entries.map(([key, value]) => [mapKey(key), value] as const);
  const reversePairs = pairs.map(([name, value]) => [value, name] as const);

  const byName = Object.freeze(Object.fromEntries(pairs)) as Readonly<Record<TName, EnumValue<E>>>;
  const byValue = Object.freeze(
    Object.fromEntries(reversePairs),
  ) as Readonly<Record<EnumValue<E>, TName>>;

  return {
    names: Object.freeze(pairs.map(([name]) => name)) as readonly TName[],
    values: Object.freeze(pairs.map(([, value]) => value)) as readonly EnumValue<E>[],
    byName,
    byValue,
    normalize(value: string | number): TName | null {
      if (typeof value === "string") {
        return hasOwn(byName, value) ? (value as TName) : null;
      }

      return hasOwn(byValue, value) ? byValue[value as EnumValue<E>] : null;
    },
    isName(value: unknown): value is TName {
      return typeof value === "string" && hasOwn(byName, value);
    },
    isValue(value: unknown): value is EnumValue<E> {
      return typeof value === "number" && Number.isInteger(value) && hasOwn(byValue, value);
    },
  };
}

function createCamelCaseEnumCodec<E extends EnumLike>(
  enumObject: E,
): EnumCodec<SnakeToCamelCase<EnumForwardKey<E>>, EnumValue<E>> {
  return createEnumCodec(enumObject, (key) => snakeToCamelCase(key) as SnakeToCamelCase<typeof key>);
}

function createIdentityEnumCodec<E extends EnumLike>(
  enumObject: E,
): EnumCodec<EnumForwardKey<E>, EnumValue<E>> {
  return createEnumCodec(enumObject, (key) => key);
}

export type SelectableSpanFieldName = SnakeToCamelCase<EnumForwardKey<typeof SelectableSpanField>>;
export type CastTypeName = SnakeToCamelCase<EnumForwardKey<typeof CastType>>;
export type DecodeStrategyName = SnakeToCamelCase<EnumForwardKey<typeof DecodeStrategy>>;
export type SpanSortFieldName = SnakeToCamelCase<EnumForwardKey<typeof SpanSortField>>;
export type AggregateMetricName = SnakeToCamelCase<EnumForwardKey<typeof AggregateMetric>>;
export type AggregateGroupFieldName = SnakeToCamelCase<EnumForwardKey<typeof AggregateGroupField>>;
export type TimeBucketName = SnakeToCamelCase<EnumForwardKey<typeof TimeBucket>>;
export type SortDirectionName = EnumForwardKey<typeof SortDirection>;

export const selectableSpanFieldCodec = createCamelCaseEnumCodec(SelectableSpanField);
export const castTypeCodec = createCamelCaseEnumCodec(CastType);
export const decodeStrategyCodec = createCamelCaseEnumCodec(DecodeStrategy);
export const spanSortFieldCodec = createCamelCaseEnumCodec(SpanSortField);
export const aggregateMetricCodec = createCamelCaseEnumCodec(AggregateMetric);
export const aggregateGroupFieldCodec = createCamelCaseEnumCodec(AggregateGroupField);
export const timeBucketCodec = createCamelCaseEnumCodec(TimeBucket);
export const sortDirectionCodec = createIdentityEnumCodec(SortDirection);
