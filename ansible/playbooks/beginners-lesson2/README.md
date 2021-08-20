# 1.gather_facts.yml

для просмотра всех фактов есть комманда

```ansible -u root -i inventories/dev/inventory web -m gather_facts --tree /tmp/fact```

В плейбуке можно запустить
```
- name: Collect facts
  setup:

- name: Output all facts on host
  debug:
    var: hostvars[inventory_hostname]
```
# 2.debug.yml
Примеры debug c с разными уровнями

#3.service_facts.yml
выполнить вывод состояния всех служб

#4.service_facts_specific.yml
вывод состояние конкретной службы

#5.service_facts_stoped.yml
вывод всех остановленных служб
