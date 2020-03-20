<p align="center">
  <br>
   <img src="https://i.imgur.com/54Ssp9c.png" width="400" alt="Python Chain Logo" title="Python Chain Logo" />
  <br>
</p>
<p align="center">
An easy to use function chaining pattern on Python.
</p>

## 📖 About this Project

Chaining functions is a common functional development pattern that is pretty difficult on Python. Usually, we need to pass some data through a pipeline, process or series of functions in order to get a specific output. Without this lib, you would need to wrap those functions on a class or assign each result on a variable.

With **python-chain** you can create an initial state and execute a chain of functions, nourishing that state during the pipeline, like this:

![Code sample](https://i.imgur.com/IHRr4C7.png)

## 🤖 Getting Started

On this section, you'll learn all the prerequisites and basic knowledge in order to use this library on your projects.

### Installation

You can install it using **pip**, running:

``` sh
pip install python-chain
```

### Common Usage

#### Creating Chainable Functions

You can chain functions by decorating them with the `@chain` decorator. Like the following:

``` python
import chain


@chain
def some_pretty_func(state):
  ...

# Now you can chain that function with the operator>>
```

#### Using State

Every chain has a `state`. That state is an Object with immutable attributes. The current Chain state will be passed automatically on the keyword argument **context**. Every chain should start with a given state, even if it empty. You can create a new one by using:

``` python
import chain

state = chain.state()
```

If you want to feed data into your initial state, you can pass then as kwargs. The key-value pair on the kwargs of your state will be passed as attributes on your chain context. Like so:

``` python
import chain

state = chain.state(foo='bar')

@chain
def test_chain(context):
  print(context.foo)
  # bar

```

#### Using States on Chains

Every mutation that you do in a chain function will add it to the next function. You can merge what you have learned both on states and functions by following:

``` python
import chain

@chain
def calculate_average(context, type='meter'):
  nbs = [house.get(type) for house in state.houses]

  context.avg = sum(nbs) / len(nbs)

@chain
def add_houses(context):
  houses = [
    { meter: 3, },
    { meter: 10, },
  ]

  context.houses = houses

result = chain.state() >> add_houses >> calculate_average
print(result.current)
#
# {
#   avg: 6.5,
#   houses: [
#     { meter: 3 },
#     { meter: 10 },
#   ]
# }
#
```

If you don't return anything on your final chain function it will automatically return the Context object. They have a lot of properties, and one of them is the `current` attribute. That will return the current state of your given context.

#### Finishing a Chain

Every time a chain is finished, it will automatically return its context. You can also add an output by retuning the data that you want on the last step of the chain, like this:

``` python
import chain

@chain
def get_name(context):
  return context.name

@chain
def add_user(context):
  context.name = 'foo'

result = chain.state() >> add_user >> get_name
print(result.output)
#
# 'foo'
#
```

#### Passing arguments directly

You can pass any args or kwargs directly to the next function. They should be passed returning a tuple with all the args on the first argument and the kwargs on the second. You can do so like this:

``` python
import chain

@chain
def store_result(result, context, type=None):
  context.result = result
  context.type = type

@chain
def add_result(context):
  args = ('foo',)
  kwargs = {type: 'bar'}

  return args, kwargs

result = chain.state() >> add_result >> store_result
print(result.current)
#
# {
#   result: 'foo',
#   type: 'bar',
# }
#
```

**Be careful**. This would create a **strong dependency** between those two functions. Chain will always pass the args and kwargs that you've created and it will break the chain if the next function doesn't accept those params. Also, always set a state params, because it will be passed by the Chain with the current state.

## ✍️ Contributing

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. You can learn how to contribute to this project on the [`CONTRIBUTING`](CONTRIBUTING.md) file.

## 🔓 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
