# Printable Procedure Checklists

## Sample Output

<img alt="A printable checklist for first aid care if someone is drunk" src="https://github.com/gdmen/printable-procedures/blob/master/sample_output.png" width="300">

## Setup
```
> make
> make run
```
Go to [localhost:5000](http://localhost:5000)

Add new checklists to `procedures/` as [Markdown](https://daringfireball.net/projects/markdown/). Only lists are styled by default.

## Special Elements

* #### citations:
  ```
  <div class="citations">
  * [source](url)
  * [source](url)
  ...
  </div>
  ```
* #### alerts:
  ```
  <i class="alert">CALL 911!</i>
  ```
