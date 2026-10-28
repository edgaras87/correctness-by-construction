# Briefing — checkout, correctness-first

## The situation

A small online shop sells goods kept in limited stock. At checkout,
the buyer's card is authorized: the money is reserved, not taken.
The shop then decides to accept or reject the order, from the stock,
the authorization, and its own limits, such as a maximum per buyer.
An accepted order has its money captured and its stock committed. A
rejected one has its authorization voided, and the buyer pays
nothing.

The payment provider is unreliable. An authorization can time out
without saying whether it went through. Its notices arrive twice,
late, or out of order. And an authorization expires: after a set
time the provider drops the reserved money, and a capture after
that fails. Buyers double-click and their apps retry, so
one checkout can arrive many times. On busy sales, many buyers try
for the last items at once.

On busy days five complaints come in: a buyer charged for an order
that was rejected; an order accepted with nothing left to ship; one
checkout that became two orders; an order whose answer changed
after the buyer was told; and an accepted order shipped with no
money behind it, its authorization expired before the capture.

The service to build is called `checkout`.

## The audience

The shop's staff, who must say for any order what was decided, when,
and why, and where its money is. And the buyers, who must never pay
for an order they did not get, and never be told yes and then no.

## The territory

In: checkout requests, retried or not; stock for the items in a
checkout; authorizing, capturing and voiding through the provider;
the one decision per order, accepted or rejected, with its reason;
the provider's notices, however they arrive; an authorization left
hanging when its outcome is unknown; an authorization that expires
before its order's capture.

Out: refunds after a capture, since returning captured money is the
staff's work with the provider; prices, discounts and tax; accounts
and sign-in; shipping; any user interface; more than one currency.
The real payment provider is out: a stand-in that misbehaves the
ways the real one does takes its place.

## The bar a promise must clear

It can be shown false by a test that creates the trouble, on one
machine: many buyers on the last items at once; the same checkout
sent many times; an authorization that times out with its outcome
unknown; a provider notice repeated, late or out of order; an
authorization expiring before its capture; the service killed
between deciding and capturing.

## The open decision

What the service promises above all: that money moves only as the
decision says, that each checkout gets exactly one decision that
never changes, or something that holds both. That is framing's to
decide, not this briefing's.
