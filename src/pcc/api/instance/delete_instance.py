# -*- coding: utf-8 -*-

def command():
    return "delete-instance"

def init_argument(parser):
    parser.add_argument("--farm-no", required=True)
    parser.add_argument("--instance-no", required=True)

def execute(requester, args):
    farm_no = args.farm_no
    instance_no = args.instance_no

    parameters = {}
    parameters["FarmNo"] = farm_no
    parameters["InstanceNo"] = instance_no

    return requester.execute("/DeleteInstance", parameters)
