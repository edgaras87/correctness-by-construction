# Briefing — event tickets, correctness-first

## The situation

A small promoter sells seats for an event at one venue. A buyer picks
seats and holds them while paying. Payment goes through an outside
payment provider, which confirms later: sometimes twice, sometimes
after a long delay, sometimes never. A hold that is not paid in time
is released, and the seat goes back on sale.

On busy sales two complaints come in: a seat sold to two people, and
a buyer charged with no ticket to show for it.

## The audience

The promoter's staff, who answer those complaints and need to say
what happened to any one seat or payment. And the buyers, who must
never be the ones who pay for a mistake.

## The territory

In: holding seats, with expiry; orders and the provider's payment
confirmations; issuing tickets; releasing expired holds; what happens
when a confirmation arrives for a seat no longer held.

Out: refunds, since returning money is the staff's work with the
provider, and the service only records who is owed; pricing; accounts
and sign-in; any user interface; more than one event on sale; resale.
The real payment provider is out: a stand-in that misbehaves the ways
the real one does takes its place.

## The bar a promise must clear

It can be shown false by a test that creates the trouble, on one
machine: many buyers on one seat at once, a confirmation late,
repeated or never sent, the service killed mid-step.

## The open decision

What the service promises above all: that a seat is never sold
twice, that no buyer pays without a ticket, or something that holds
both. That is framing's to decide, not this briefing's.
