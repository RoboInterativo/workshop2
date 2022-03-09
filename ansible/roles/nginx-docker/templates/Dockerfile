FROM nginx
EXPOSE 443 80

RUN {% for item in params   %} {% if item.sub==False %} mkdir /etc/letsencrypt/live/{{ item.site }}/ -p  &&  {% endif %}  {% endfor %}echo 'work around FIX last.loop'


COPY files/options-ssl-nginx.conf files/ssl-dhparams.pem /etc/letsencrypt/
{% for item in params %}
{% if item.sub==False %}
COPY files/{{ item.site }}/fullchain.pem files/{{ item.site }}/privkey.pem /etc/letsencrypt/live/{{ item.site }}/ 
{% endif %}
{% endfor %}
COPY files/site.conf   /etc/nginx/conf.d/

RUN apt-get update && apt-get install -y locales

# Locale
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen

ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

# +Timezone (е�^aли надо на �^m�^bапе �^aбо�^`ки)
ENV TZ Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo TEST BUILD

