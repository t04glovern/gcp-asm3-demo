def GenerateConfig(context):
    """Generate YAML resource configuration."""

    cluster_types_root = ''.join([
        context.env['project'],
        '/',
        context.properties['clusterType']
    ])
    cluster_types = {
        'Service': ''.join([
            cluster_types_root,
            ':',
            '/api/v1/namespaces/{namespace}/services'
        ]),
        'Deployment': ''.join([
            cluster_types_root,
            '-apps',
            ':',
            '/apis/apps/v1beta1/namespaces/{namespace}/deployments'
        ]),
        'PersistentVolumeClaim': ''.join([
            cluster_types_root,
            ':',
            '/api/v1/namespaces/{namespace}/persistentvolumeclaims'
        ]),
    }

    name_prefix = context.env['deployment'] + '-' + context.env['name']
    port = context.properties['port']
    postgres_user = context.properties['postgresUser']
    postgres_pass = context.properties['postgresPass']
    postgres_db = context.properties['postgresDb']

    resources = [{
        'name': name_prefix + '-service',
        'type': cluster_types['Service'],
        'properties': {
            'apiVersion': 'v1',
            'kind': 'Service',
            'namespace': 'default',
            'metadata': {
                'name': name_prefix + '-service',
                'labels': {
                    'id': 'deployment-manager'
                }
            },
            'spec': {
                'type': 'ClusterIP',
                'ports': [{
                    'port': port
                }],
                'selector': {
                    'app': name_prefix
                }
            }
        }
    }, {
        'name': name_prefix + '-pv-claim',
        'type': cluster_types['PersistentVolumeClaim'],
        'properties': {
            'apiVersion': 'v1',
            'kind': 'PersistentVolumeClaim',
            'namespace': 'default',
            'metadata': {
                'name': name_prefix + '-pv-claim',
                'labels': {
                    'id': 'deployment-manager'
                }
            },
            'spec': {
                'accessModes': [
                    'ReadWriteOnce'
                ],
                'resources': {
                    'requests': {
                        'storage': '8Gi'
                    }
                }
            }
        }
    }, {
        'name': name_prefix + '-deployment',
        'type': cluster_types['Deployment'],
        'properties': {
            'apiVersion': 'apps/v1beta1',
            'kind': 'Deployment',
            'namespace': 'default',
            'metadata': {
                'name': name_prefix + '-deployment'
            },
            'spec': {
                'replicas': 1,
                'template': {
                    'metadata': {
                        'labels': {
                            'name': name_prefix + '-deployment',
                            'app': name_prefix
                        }
                    },
                    'spec': {
                        'volumes': [{
                            'name': name_prefix + '-storage',
                            'persistentVolumeClaim': {
                                'claimName': name_prefix + '-pv-claim'
                            }
                        }],
                        'containers': [{
                            'name': name_prefix + '-container',
                            'image': context.properties['image'],
                            'env': [{
                                'name': 'POSTGRES_USER',
                                'value': postgres_user
                            }, {
                                'name': 'POSTGRES_PASSWORD',
                                'value': postgres_pass
                            }, {
                                'name': 'POSTGRES_DB',
                                'value': postgres_db
                            }, {
                                'name': 'PGDATA',
                                'value': '/var/lib/postgresql/data/pgdata'
                            }],
                            'ports': [{
                                'containerPort': port
                            }],
                            'volumeMounts': [{
                                'name': name_prefix + '-storage',
                                'mountPath': '/var/lib/postgresql/data'
                            }]
                        }]
                    }
                }
            }
        }
    }]

    return {'resources': resources}
