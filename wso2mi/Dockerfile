FROM wso2/wso2mi:4.2.0

COPY car-files/wso2mi_1.0.0.car /home/wso2carbon/wso2mi/repository/deployment/server/carbonapps/

USER root
RUN chown -R wso2carbon:wso2 /home/wso2carbon/wso2mi/repository/deployment/server/carbonapps/
RUN rm -rf /home/wso2carbon/wso2mi/repository/deployment/server/synapse-configs/default/*
RUN rm -rf /home/wso2carbon/wso2mi/repository/deployment/server/carbonapps/.metafiles

USER wso2carbon
